#!/usr/bin/env python3
"""Fix double headings in research papers.

Pattern: ## Chapter N: ... followed (within a few lines) by # Chapter N: ...
The duplicate # heading should be removed. The ## heading + image stays.
"""

import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESEARCH_DIR = os.path.join(REPO_ROOT, "content", "research")


def fix_double_headings(filepath: str) -> int:
    """Remove duplicate # headings. Returns count removed."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern: ## Chapter/Abstract/Conclusion heading exists,
    # then within next few lines, a # heading with same section appears
    # We want to remove the standalone # heading line

    lines = content.split('\n')
    to_remove = set()
    removed = 0

    for i, line in enumerate(lines):
        # Look for ## Chapter N: heading
        h2_match = re.match(r'^##\s+((?:Chapter\s+\d+|Abstract|Conclusion|Introduction|Discussion|Methodology|Results|References|Appendix)[^#]*)', line)
        if h2_match:
            h2_key = re.match(r'(Chapter\s+\d+|Abstract|Conclusion|Introduction|Discussion|Methodology|Results|References|Appendix)', h2_match.group(1).strip(), re.IGNORECASE)
            if h2_key:
                section_id = h2_key.group(1).lower()
                # Look ahead up to 6 lines for the duplicate # heading
                for j in range(i + 1, min(i + 7, len(lines))):
                    h1_match = re.match(r'^#\s+((?:Chapter\s+\d+|Abstract|Conclusion|Introduction|Discussion|Methodology|Results|References|Appendix)[^#]*)', lines[j])
                    if h1_match:
                        h1_key = re.match(r'(Chapter\s+\d+|Abstract|Conclusion|Introduction|Discussion|Methodology|Results|References|Appendix)', h1_match.group(1).strip(), re.IGNORECASE)
                        if h1_key and h1_key.group(1).lower() == section_id:
                            to_remove.add(j)
                            removed += 1
                            break

    if to_remove:
        new_lines = [line for idx, line in enumerate(lines) if idx not in to_remove]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))

    return removed


def main():
    total_fixed = 0
    files_fixed = 0

    for fname in sorted(os.listdir(RESEARCH_DIR)):
        if not fname.endswith('.md') or fname.startswith('_'):
            continue
        filepath = os.path.join(RESEARCH_DIR, fname)
        count = fix_double_headings(filepath)
        if count > 0:
            files_fixed += 1
            total_fixed += count
            print(f"  Fixed {count} duplicate headings in: {fname}")

    print(f"\n=== Double Heading Fix Complete ===")
    print(f"Files fixed: {files_fixed}")
    print(f"Total duplicate headings removed: {total_fixed}")


if __name__ == '__main__':
    main()
