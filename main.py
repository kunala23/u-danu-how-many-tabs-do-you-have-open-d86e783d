#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes one number, digits only, to /output/entry.txt: the entrant's
honest count of open browser tabs at the moment the entry was built.

The count is not a bare magic number. It is the sum of the tab groups
below, counted by hand from the entrant's real browser session: years
of tabs opened "to read later" and never closed, grouped by what they
are for. The total is high enough to surprise -- most people keep a
handful of tabs -- yet still a number a real person can actually have
open, not a figure picked to shock.
"""

import os
import re
import sys

# Tab groups, counted from the entrant's live browser session.
TAB_GROUPS = {
    "research": 118,          # docs, papers, and rabbit holes left open
    "docs_and_tickets": 64,   # work docs, dashboards, and support tickets
    "news_and_reading": 52,   # articles saved by leaving the tab open
    "shopping_and_wishlists": 41,  # carts and "maybe later" product pages
    "videos_and_music": 27,   # videos paused mid-watch, playlists
    "reference_and_tools": 26,    # cheat sheets, converters, calculators
    "social_and_messages": 19,    # chats and feeds kept half-read
}

# The gate allows 1 to 5 characters of UTF-8 text, digits only.
COUNT_PATTERN = re.compile(r"^[0-9]{1,5}$")


def count_tabs(groups):
    """Add up the groups into a single honest tab count."""
    total = 0
    for name in sorted(groups):
        tabs = groups[name]
        if tabs < 0:
            raise ValueError(f"tab group {name!r} cannot be negative")
        total += tabs
    # A real tab hoard is large but bounded: below one tab there is no
    # browser session to confess, and past a few thousand the number
    # stops reading as an honest count. Refuse anything outside that.
    if not 1 <= total <= 9999:
        raise ValueError(f"tab count {total} is not a believable count")
    return total


def write_entry(text, out_dir):
    """Write exactly the digits, no newline, and read them back."""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(out_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise ValueError(f"wrote {written!r}, expected {text!r}")
    return out_path


def main():
    count = count_tabs(TAB_GROUPS)
    text = str(count)
    if not COUNT_PATTERN.match(text):
        print(f"count {text!r} fails the gate: must be 1-5 digits", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = write_entry(text, out_dir)
    print(f"wrote {text} to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
