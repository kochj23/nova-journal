#!/usr/bin/env python3
"""Fix truncated descriptions in front matter.

If a description ends mid-word (not at a natural boundary like . ! ? " ...),
truncate at the last complete word and add "..."
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(REPO_ROOT, "content")

# Natural endings that indicate the description is complete
NATURAL_ENDINGS = re.compile(r'[.!?"…]$')


def fix_description(desc: str) -> str:
    """Fix a truncated description by trimming to last complete word."""
    desc = desc.strip()
    if not desc:
        return desc

    # Remove surrounding quotes if present
    if desc.startswith('"') and desc.endswith('"'):
        inner = desc[1:-1]
        if NATURAL_ENDINGS.search(inner):
            return desc  # Already ends properly
        # Truncate at last space
        last_space = inner.rfind(' ')
        if last_space > 0:
            return '"' + inner[:last_space] + '..."'
        return desc
    elif desc.startswith('"'):
        # Has opening quote but no closing quote (truncated)
        inner = desc[1:]
        if NATURAL_ENDINGS.search(inner):
            return desc + '"'
        last_space = inner.rfind(' ')
        if last_space > 0:
            return '"' + inner[:last_space] + '..."'
        return desc

    # No quotes
    if NATURAL_ENDINGS.search(desc):
        return desc
    last_space = desc.rfind(' ')
    if last_space > 0:
        return desc[:last_space] + "..."
    return desc


def process_file(filepath: str) -> bool:
    """Process a single markdown file. Returns True if modified."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Only process files with YAML front matter
    if not content.startswith('---'):
        return False

    # Find end of front matter
    end_idx = content.find('---', 3)
    if end_idx == -1:
        return False

    front_matter = content[3:end_idx]
    body = content[end_idx:]

    # Find description line
    desc_pattern = re.compile(r'^(description:\s*)(".*?"|\'.*?\'|.*?)$', re.MULTILINE)
    match = desc_pattern.search(front_matter)
    if not match:
        return False

    prefix = match.group(1)
    original_desc = match.group(2)

    # Handle quoted descriptions
    if original_desc.startswith('"'):
        # Check if it's a properly closed quote
        if original_desc.endswith('"') and len(original_desc) > 2:
            inner = original_desc[1:-1]
            if NATURAL_ENDINGS.search(inner):
                return False
            # Truncated inside quotes
            last_space = inner.rfind(' ')
            if last_space > 0:
                fixed = '"' + inner[:last_space] + '..."'
            else:
                return False
        elif not original_desc.endswith('"'):
            # Missing closing quote — definitely truncated
            inner = original_desc[1:]
            last_space = inner.rfind(' ')
            if last_space > 0:
                fixed = '"' + inner[:last_space] + '..."'
            else:
                fixed = original_desc + '..."'
        else:
            return False
    else:
        # Unquoted description
        if NATURAL_ENDINGS.search(original_desc.strip()):
            return False
        desc_stripped = original_desc.strip()
        last_space = desc_stripped.rfind(' ')
        if last_space > 0:
            fixed = '"' + desc_stripped[:last_space] + '..."'
        else:
            return False

    if fixed == original_desc:
        return False

    new_front_matter = front_matter[:match.start(2) - 3] + prefix + fixed + front_matter[match.end():]
    # Reconstruct properly
    new_front_matter = front_matter.replace(prefix + original_desc, prefix + fixed, 1)

    new_content = '---' + new_front_matter + body

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def main():
    fixed_count = 0
    total_count = 0

    for root, dirs, files in os.walk(CONTENT_DIR):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            filepath = os.path.join(root, fname)
            total_count += 1
            if process_file(filepath):
                fixed_count += 1
                print(f"  Fixed: {os.path.relpath(filepath, REPO_ROOT)}")

    print(f"\n=== Description Fix Complete ===")
    print(f"Files scanned: {total_count}")
    print(f"Descriptions fixed: {fixed_count}")


if __name__ == '__main__':
    main()
