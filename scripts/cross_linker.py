#!/usr/bin/env python3
"""Semantic Cross-Linker — finds related posts using pgvector embeddings.

Reads all published .md files, generates embeddings for title+description,
queries pgvector for nearest neighbors, and writes `related:` front matter
(top 3 matches) back into each file.

The template `layouts/partials/related_posts.html` renders these links.

Requirements:
  pip install psycopg2-binary numpy

Usage:
  python3 scripts/cross_linker.py

Environment:
  NOVA_DB_HOST (default: 127.0.0.1)
  NOVA_DB_PORT (default: 5432)
  NOVA_DB_NAME (default: nova_memories)
  NOVA_DB_USER (default: kochj)
  OLLAMA_URL (default: http://127.0.0.1:11434)
"""

import os
import re
import sys
import json
import urllib.request
import urllib.error
from typing import Optional

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(REPO_ROOT, "content")

# Configuration
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434")
EMBED_MODEL = "nomic-embed-text"
TOP_K = 3  # Number of related posts to suggest

DB_CONFIG = {
    "host": os.environ.get("NOVA_DB_HOST", "127.0.0.1"),
    "port": int(os.environ.get("NOVA_DB_PORT", "5432")),
    "dbname": os.environ.get("NOVA_DB_NAME", "nova_memories"),
    "user": os.environ.get("NOVA_DB_USER", "kochj"),
}


def get_embedding(text: str) -> Optional[list]:
    """Get embedding from Ollama."""
    try:
        payload = json.dumps({"model": EMBED_MODEL, "input": text}).encode()
        req = urllib.request.Request(
            f"{OLLAMA_URL}/api/embed",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            if "embeddings" in data and data["embeddings"]:
                return data["embeddings"][0]
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        print(f"  WARN: Embedding failed: {e}")
    return None


def parse_front_matter(content: str) -> tuple:
    """Parse YAML front matter. Returns (front_matter_str, body_str, end_idx)."""
    if not content.startswith('---'):
        return None, content, 0
    end_idx = content.find('---', 3)
    if end_idx == -1:
        return None, content, 0
    return content[3:end_idx], content[end_idx + 3:], end_idx


def extract_metadata(filepath: str) -> Optional[dict]:
    """Extract title, description, category, and URL slug from a markdown file."""
    basename = os.path.basename(filepath)

    # Skip structural files that shouldn't get related links
    if basename in ('_index.md', 'search.md'):
        return None

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, _, _ = parse_front_matter(content)
    if fm is None:
        return None

    title_match = re.search(r'^title:\s*"((?:[^"\\]|\\.)*)"', fm, re.MULTILINE)
    desc_match = re.search(r'^description:\s*"((?:[^"\\]|\\.)*)"', fm, re.MULTILINE)
    cat_match = re.search(r'^categories:\s*\["([^"]*)"', fm, re.MULTILINE)
    draft_match = re.search(r'^draft:\s*(true|false)', fm, re.MULTILINE)

    if draft_match and draft_match.group(1) == 'true':
        return None

    title = title_match.group(1).replace('\\"', '"') if title_match else ""
    desc = desc_match.group(1).replace('\\"', '"') if desc_match else ""
    category = cat_match.group(1) if cat_match else ""

    # Derive URL from file path
    rel = os.path.relpath(filepath, CONTENT_DIR)
    # Remove .md extension and handle index files
    if rel.endswith('/index.md'):
        url_path = '/' + rel.rsplit('/index.md', 1)[0] + '/'
    else:
        url_path = '/' + rel.replace('.md', '/').replace('_index', '')

    return {
        "filepath": filepath,
        "title": title,
        "description": desc,
        "category": category,
        "url": url_path,
        "embed_text": f"{title}. {desc}",
    }


def write_related(filepath: str, related: list):
    """Write related posts into the front matter of a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---\n'):
        return

    # Find closing --- on its own line
    # Split into lines and find the second ---
    lines = content.split('\n')
    end_line = None
    for i in range(1, len(lines)):
        if lines[i] == '---':
            end_line = i
            break

    if end_line is None:
        return

    fm_lines = lines[1:end_line]
    body_lines = lines[end_line:]  # starts with ---

    # Remove existing related: block
    new_fm_lines = []
    i = 0
    while i < len(fm_lines):
        if fm_lines[i].startswith('related:'):
            # Skip related: line and all subsequent indented lines
            i += 1
            while i < len(fm_lines) and (fm_lines[i].startswith('  ') or fm_lines[i].startswith('\t') or fm_lines[i] == ''):
                i += 1
            continue
        new_fm_lines.append(fm_lines[i])
        i += 1

    # Build related YAML lines
    related_lines = ["related:"]
    for r in related:
        title = r['title']
        if '"' in title:
            title_escaped = title.replace("'", "''")
            title_field = f"'{title_escaped}'"
        else:
            title_field = f'"{title}"'
        related_lines.append(f'  - title: {title_field}')
        related_lines.append(f'    url: "{r["url"]}"')
        related_lines.append(f'    category: "{r["category"]}"')

    # Combine: opening ---, front matter, related block, closing ---
    all_lines = ['---'] + new_fm_lines + related_lines + body_lines
    new_content = '\n'.join(all_lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)


def cosine_similarity(a: list, b: list) -> float:
    """Compute cosine similarity between two vectors."""
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(x * x for x in b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def main():
    print("=== Semantic Cross-Linker ===")
    print(f"Embedding model: {EMBED_MODEL}")
    print(f"Ollama URL: {OLLAMA_URL}")
    print("")

    # Step 1: Collect all posts
    posts = []
    for root, dirs, files in os.walk(CONTENT_DIR):
        for fname in sorted(files):
            if not fname.endswith('.md') or fname.startswith('_'):
                continue
            filepath = os.path.join(root, fname)
            meta = extract_metadata(filepath)
            if meta and meta['title']:
                posts.append(meta)

    print(f"Found {len(posts)} published posts")

    # Step 2: Generate embeddings
    print("Generating embeddings...")
    embeddings = {}
    for i, post in enumerate(posts):
        emb = get_embedding(post['embed_text'])
        if emb:
            embeddings[post['filepath']] = emb
        if (i + 1) % 20 == 0:
            print(f"  {i + 1}/{len(posts)} embedded")

    print(f"Got embeddings for {len(embeddings)}/{len(posts)} posts")

    if len(embeddings) < 5:
        print("ERROR: Too few embeddings generated. Is Ollama running?")
        print("Cross-linking requires the Ollama embedding server.")
        print("Run manually when Ollama is available.")
        sys.exit(0)  # Don't fail the build

    # Step 3: Find nearest neighbors for each post
    print("Finding related posts...")
    updates = 0
    for post in posts:
        if post['filepath'] not in embeddings:
            continue

        current_emb = embeddings[post['filepath']]
        current_cat = post['category']

        # Score all other posts (prefer cross-category)
        scores = []
        for other in posts:
            if other['filepath'] == post['filepath']:
                continue
            if other['filepath'] not in embeddings:
                continue

            sim = cosine_similarity(current_emb, embeddings[other['filepath']])
            # Boost cross-category links slightly
            if other['category'] != current_cat:
                sim *= 1.05
            scores.append((sim, other))

        # Top K
        scores.sort(key=lambda x: x[0], reverse=True)
        related = [
            {"title": s[1]['title'], "url": s[1]['url'], "category": s[1]['category']}
            for s in scores[:TOP_K]
        ]

        if related:
            write_related(post['filepath'], related)
            updates += 1

    print(f"\nUpdated {updates} posts with related links")
    print("=== Cross-Linking Complete ===")


if __name__ == '__main__':
    main()
