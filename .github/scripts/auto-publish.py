#!/usr/bin/env python3
"""
Auto-Publish Script — 扫描 content/ 目录，找到 hidden: true 且 publishDate 到期的文章，
自动删除 hidden: true 和 publishDate 字段，实现自动发布。

SOP 08 定时发布机制：
- 每天检查，publishDate 到期即发布
- 仅修改到期文章，不动其他文章
- 自动更新 lastmod 为非整点时间
"""

import os
import re
import sys
import yaml
from datetime import datetime, timezone

CONTENT_DIR = "content"

def parse_frontmatter(text):
    """Parse YAML frontmatter from markdown text."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', text, re.DOTALL)
    if not m:
        return None, text
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        fm = {}
    return fm or {}, m.group(2)

def build_frontmatter(fm):
    """Build frontmatter string from dict."""
    lines = ["---"]
    for key, value in fm.items():
        if isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, (int, float)):
            lines.append(f"{key}: {value}")
        elif isinstance(value, list):
            items = yaml.dump({key: value}, default_flow_style=False).strip()
            lines.append(items)
        elif isinstance(value, str):
            if any(c in value for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '!', '|', '>', "'", '"']):
                lines.append(f'{key}: "{value}"')
            else:
                lines.append(f"{key}: {value}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)

def main():
    now = datetime.now(timezone.utc)
    published = []

    for root, dirs, files in os.walk(CONTENT_DIR):
        for fname in files:
            if not fname.endswith(".md"):
                continue

            fpath = os.path.join(root, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                raw = f.read()

            fm, body = parse_frontmatter(raw)
            if fm is None:
                continue

            # Skip articles without hidden flag or publishDate
            if not fm.get("hidden", False):
                continue
            if "publishDate" not in fm:
                continue

            pub_str = fm["publishDate"]
            if isinstance(pub_str, datetime):
                pub_dt = pub_str
            else:
                try:
                    # Try various formats
                    for fmt in [
                        "%Y-%m-%dT%H:%M:%S%z",
                        "%Y-%m-%dT%H:%M:%S",
                        "%Y-%m-%d",
                    ]:
                        try:
                            pub_dt = datetime.strptime(pub_str, fmt)
                            if pub_dt.tzinfo is None:
                                pub_dt = pub_dt.replace(tzinfo=timezone.utc)
                            break
                        except ValueError:
                            continue
                    else:
                        print(f"  [SKIP] {fname}: unrecognized publishDate format: {pub_str}")
                        continue
                except Exception as e:
                    print(f"  [SKIP] {fname}: parse error - {e}")
                    continue

            if pub_dt > now:
                print(f"  [WAIT] {fname}: publishDate {pub_dt} is in the future")
                continue

            # 🎯 Publish! Remove hidden and publishDate
            del fm["hidden"]
            del fm["publishDate"]

            # Update lastmod to non-hour time (simulate human edit)
            from random import randint
            non_hour = now.replace(
                hour=randint(8, 22),
                minute=randint(1, 59),
                second=randint(1, 59)
            )
            fm["lastmod"] = non_hour.strftime("%Y-%m-%dT%H:%M:%S%z")

            # Rebuild file
            new_fm_str = build_frontmatter(fm)
            new_content = new_fm_str + "\n" + body

            # Remove trailing blank lines from end, keep one
            new_content = new_content.rstrip("\n") + "\n"

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"  ✅ PUBLISHED: {fname}")
            published.append(fpath)

    if published:
        print(f"\nTotal published: {len(published)}")
    else:
        print("No articles ready for publishing.")

if __name__ == "__main__":
    main()
