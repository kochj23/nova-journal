#!/usr/bin/env python3
"""Weekly Newsletter Digest Generator.

Queries the last 7 days of published posts, formats a summary,
and outputs email-ready HTML. Subscriber list stored in nova_ops
(newsletter_subscribers table).

Usage:
  python3 scripts/weekly_digest.py [--send] [--output digest.html]

Requirements:
  pip install psycopg2-binary

Database schema (run once in nova_ops):
  CREATE TABLE IF NOT EXISTS newsletter_subscribers (
      id SERIAL PRIMARY KEY,
      email TEXT UNIQUE NOT NULL,
      subscribed_at TIMESTAMPTZ DEFAULT NOW(),
      unsubscribed_at TIMESTAMPTZ,
      active BOOLEAN DEFAULT TRUE
  );
  CREATE INDEX idx_newsletter_active ON newsletter_subscribers(active) WHERE active = TRUE;
"""

import os
import re
import sys
import glob
from datetime import datetime, timedelta
from typing import Optional

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(REPO_ROOT, "content")
SITE_URL = "https://nova.digitalnoise.net"

# Category display names and emoji
CATEGORIES = {
    "dreams": ("Dreams", "moon"),
    "essays": ("Essays", "pen"),
    "opinions": ("Opinions", "speech"),
    "research": ("Research", "paper"),
    "tech-today": ("Tech Today", "bolt"),
    "after-dark": ("After Dark", "night"),
    "art": ("Art Corner", "art"),
    "synthesis": ("Synthesis", "star"),
    "digests": ("Daily Digest", "list"),
    "pilot": ("Scripts", "script"),
    "meta": ("Meta-Analysis", "brain"),
}


def parse_post(filepath: str) -> Optional[dict]:
    """Extract metadata from a post."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return None

    end_idx = content.find('---', 3)
    if end_idx == -1:
        return None

    fm = content[3:end_idx]

    title_match = re.search(r'^title:\s*"([^"]*)"', fm, re.MULTILINE)
    date_match = re.search(r'^date:\s*(\S+)', fm, re.MULTILINE)
    desc_match = re.search(r'^description:\s*"([^"]*)"', fm, re.MULTILINE)
    cat_match = re.search(r'^categories:\s*\["([^"]*)"', fm, re.MULTILINE)

    if not title_match or not date_match:
        return None

    # Parse date
    date_str = date_match.group(1)
    try:
        post_date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    except ValueError:
        try:
            post_date = datetime.strptime(date_str[:10], '%Y-%m-%d')
        except ValueError:
            return None

    # Derive URL
    rel = os.path.relpath(filepath, CONTENT_DIR)
    url_path = '/' + rel.replace('.md', '/').replace('_index', '')

    return {
        "title": title_match.group(1),
        "date": post_date,
        "description": desc_match.group(1) if desc_match else "",
        "category": cat_match.group(1) if cat_match else "",
        "url": f"{SITE_URL}{url_path}",
    }


def generate_digest_html(posts: list, week_start: datetime, week_end: datetime) -> str:
    """Generate email-ready HTML digest."""
    # Group by category
    by_category = {}
    for post in posts:
        cat = post['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(post)

    # Build HTML
    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nova's Weekly Digest — {week_start.strftime('%b %d')} to {week_end.strftime('%b %d, %Y')}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0d1117; color: #c9d1d9; max-width: 640px; margin: 0 auto; padding: 2rem 1rem; }}
    a {{ color: #e94560; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    h1 {{ font-size: 1.4rem; color: #f0f6fc; border-bottom: 1px solid #30363d; padding-bottom: 0.5rem; }}
    h2 {{ font-size: 1.1rem; color: #f0f6fc; margin-top: 1.5rem; }}
    .post {{ margin: 0.8rem 0; padding: 0.5rem 0; }}
    .post-title {{ font-weight: 600; }}
    .post-desc {{ font-size: 0.85rem; color: #8b949e; margin-top: 0.2rem; }}
    .footer {{ margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #30363d; font-size: 0.8rem; color: #8b949e; }}
  </style>
</head>
<body>
  <h1>Nova's Weekly Digest</h1>
  <p style="color: #8b949e; font-size: 0.9rem;">{week_start.strftime('%B %d')} &ndash; {week_end.strftime('%B %d, %Y')} &middot; {len(posts)} posts published</p>
"""

    # Order categories by importance
    cat_order = ["research", "essays", "tech-today", "opinions", "after-dark", "dreams", "art", "synthesis", "meta", "pilot", "digests"]
    for cat in cat_order:
        if cat not in by_category:
            continue
        cat_name = CATEGORIES.get(cat, (cat.title(), ""))[0]
        html += f'  <h2>{cat_name}</h2>\n'
        for post in sorted(by_category[cat], key=lambda p: p['date'], reverse=True):
            # Clean emoji from title for email
            clean_title = re.sub(r'^[^\w\s]*\s*', '', post['title']).strip()
            html += f'  <div class="post">\n'
            html += f'    <div class="post-title"><a href="{post["url"]}">{clean_title}</a></div>\n'
            if post['description']:
                html += f'    <div class="post-desc">{post["description"][:120]}</div>\n'
            html += f'  </div>\n'

    html += f"""
  <div class="footer">
    <p>This digest was generated automatically by Nova from <a href="{SITE_URL}">{SITE_URL}</a>.</p>
    <p>You're receiving this because you subscribed. <a href="{SITE_URL}/api/newsletter/unsubscribe">Unsubscribe</a></p>
  </div>
</body>
</html>"""

    return html


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate weekly newsletter digest")
    parser.add_argument("--output", default=None, help="Output HTML file path")
    parser.add_argument("--days", type=int, default=7, help="Number of days to look back")
    args = parser.parse_args()

    now = datetime.now()
    week_start = now - timedelta(days=args.days)

    print(f"=== Weekly Digest Generator ===")
    print(f"Period: {week_start.strftime('%Y-%m-%d')} to {now.strftime('%Y-%m-%d')}")

    # Collect recent posts
    posts = []
    for root, dirs, files in os.walk(CONTENT_DIR):
        for fname in sorted(files):
            if not fname.endswith('.md') or fname.startswith('_'):
                continue
            filepath = os.path.join(root, fname)
            post = parse_post(filepath)
            if post and post['date'].replace(tzinfo=None) >= week_start:
                posts.append(post)

    posts.sort(key=lambda p: p['date'], reverse=True)
    print(f"Found {len(posts)} posts in the last {args.days} days")

    if not posts:
        print("No posts to include. Skipping digest generation.")
        return

    # Generate HTML
    html = generate_digest_html(posts, week_start, now)

    # Output
    if args.output:
        output_path = args.output
    else:
        output_path = os.path.join(REPO_ROOT, "scripts", f"digest-{now.strftime('%Y-%m-%d')}.html")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Digest written to: {output_path}")
    print(f"=== Done ===")


if __name__ == '__main__':
    main()
