#!/usr/bin/env python3
"""Remove stopword tags from all posts.

Removes tags that are common stopwords (single-word tags that carry no semantic value).
"""

import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(REPO_ROOT, "content")

STOPWORDS = {
    "like", "the", "something", "they", "didn", "and", "that", "this",
    "with", "for", "are", "but", "not", "you", "all", "can", "had",
    "her", "was", "one", "our", "its", "has", "been", "from", "will",
    "would", "could", "should", "just", "more", "also", "than", "then",
    "very", "too", "here", "there", "when", "where", "what", "which",
    "who", "whom", "how", "why", "each", "every", "both", "few", "many",
    "some", "any", "other", "into", "over", "after", "before", "between",
    "through", "about", "again", "being", "does", "doing", "done",
}


def process_file(filepath: str) -> int:
    """Remove stopword tags from a file. Returns count of tags removed."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return 0

    end_idx = content.find('---', 3)
    if end_idx == -1:
        return 0

    front_matter = content[3:end_idx]
    body = content[end_idx:]

    # Find tags line — could be YAML list format
    # Format 1: tags: ["tag1", "tag2", "tag3"]
    # Format 2: tags:\n  - tag1\n  - tag2
    tags_match = re.search(r'^tags:\s*\[([^\]]*)\]', front_matter, re.MULTILINE)
    if tags_match:
        tags_str = tags_match.group(1)
        # Parse tags
        tags = [t.strip().strip('"').strip("'") for t in tags_str.split(',')]
        original_count = len(tags)

        # Filter out stopwords
        filtered = [t for t in tags if t.lower() not in STOPWORDS and t.strip()]
        removed = original_count - len(filtered)

        if removed > 0:
            # Rebuild tags line
            new_tags_str = ', '.join(f'"{t}"' for t in filtered)
            new_front_matter = front_matter[:tags_match.start(1)] + new_tags_str + front_matter[tags_match.end(1):]
            new_content = '---' + new_front_matter + body
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return removed

    # Format 2: YAML list
    tags_list_match = re.search(r'^tags:\s*\n((?:\s+-\s+.*\n?)+)', front_matter, re.MULTILINE)
    if tags_list_match:
        tag_lines = tags_list_match.group(1)
        tags = re.findall(r'^\s+-\s+"?([^"\n]+)"?\s*$', tag_lines, re.MULTILINE)
        original_count = len(tags)
        filtered = [t for t in tags if t.lower() not in STOPWORDS and t.strip()]
        removed = original_count - len(filtered)

        if removed > 0:
            new_tag_lines = ''.join(f'  - "{t}"\n' for t in filtered)
            new_front_matter = front_matter[:tags_list_match.start(1)] + new_tag_lines + front_matter[tags_list_match.end(1):]
            new_content = '---' + new_front_matter + body
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return removed

    return 0


def main():
    total_removed = 0
    files_fixed = 0

    for root, dirs, files in os.walk(CONTENT_DIR):
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            filepath = os.path.join(root, fname)
            removed = process_file(filepath)
            if removed > 0:
                files_fixed += 1
                total_removed += removed
                print(f"  Removed {removed} stopword tags from: {os.path.relpath(filepath, REPO_ROOT)}")

    print(f"\n=== Stopword Tag Removal Complete ===")
    print(f"Files modified: {files_fixed}")
    print(f"Total stopword tags removed: {total_removed}")


if __name__ == '__main__':
    main()
