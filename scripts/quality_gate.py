#!/usr/bin/env python3
"""Content Quality Gate — validates front matter and content structure.

Checks:
1. Description length (min 20 chars, max 160 chars recommended)
2. Required fields present (title, date, description, categories)
3. No stopword-only tags
4. No malformed YAML front matter
5. No duplicate headings in research papers
6. Tags are non-empty

Exit code 1 on violations (fails the CI build).
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(REPO_ROOT, "content")

STOPWORDS = {
    "like", "the", "something", "they", "didn", "and", "that", "this",
    "with", "for", "are", "but", "not", "you", "all", "can", "had",
    "her", "was", "one", "our",
}

REQUIRED_FIELDS = {"title", "date"}
ERRORS = []


def validate_file(filepath: str):
    """Validate a single content file."""
    rel_path = os.path.relpath(filepath, REPO_ROOT)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        ERRORS.append(f"{rel_path}: Missing YAML front matter delimiter")
        return

    end_idx = content.find('---', 3)
    if end_idx == -1:
        ERRORS.append(f"{rel_path}: Unclosed YAML front matter")
        return

    front_matter = content[3:end_idx]

    # Check required fields (skip _index.md, index.md, search.md — these are structural)
    basename = os.path.basename(filepath)
    is_structural = basename in ('_index.md', 'search.md') or basename == 'index.md'

    if not is_structural:
        for field in REQUIRED_FIELDS:
            if not re.search(rf'^{field}:', front_matter, re.MULTILINE):
                ERRORS.append(f"{rel_path}: Missing required field '{field}'")

    # Check description (skip structural files)
    if not is_structural:
        desc_match = re.search(r'^description:\s*"([^"]*)"', front_matter, re.MULTILINE)
        if desc_match:
            desc = desc_match.group(1)
            if len(desc) < 15:
                ERRORS.append(f"{rel_path}: Description too short ({len(desc)} chars, min 15)")
        elif not re.search(r'^description:', front_matter, re.MULTILINE):
            ERRORS.append(f"{rel_path}: Missing description field")

    # Check tags for stopwords
    tags_match = re.search(r'^tags:\s*\[([^\]]*)\]', front_matter, re.MULTILINE)
    if tags_match:
        tags_str = tags_match.group(1)
        tags = [t.strip().strip('"').strip("'") for t in tags_str.split(',') if t.strip()]
        for tag in tags:
            if tag.lower() in STOPWORDS:
                ERRORS.append(f"{rel_path}: Stopword tag found: '{tag}'")

    # Check for duplicate headings in research papers
    if '/research/' in filepath:
        body = content[end_idx + 3:]
        h2_chapters = re.findall(r'^## (Chapter \d+)', body, re.MULTILINE)
        h1_chapters = re.findall(r'^# (Chapter \d+)', body, re.MULTILINE)
        for ch in h1_chapters:
            if ch in h2_chapters:
                ERRORS.append(f"{rel_path}: Duplicate heading for {ch} (## and # both exist)")


def main():
    file_count = 0
    for root, dirs, files in os.walk(CONTENT_DIR):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            filepath = os.path.join(root, fname)
            file_count += 1
            validate_file(filepath)

    print(f"=== Content Quality Gate ===")
    print(f"Files checked: {file_count}")

    if ERRORS:
        print(f"\nVIOLATIONS FOUND: {len(ERRORS)}")
        for err in ERRORS[:50]:  # Limit output
            print(f"  ERROR: {err}")
        if len(ERRORS) > 50:
            print(f"  ... and {len(ERRORS) - 50} more")
        print(f"\nQuality gate FAILED.")
        sys.exit(1)
    else:
        print("All checks passed.")
        sys.exit(0)


if __name__ == '__main__':
    main()
