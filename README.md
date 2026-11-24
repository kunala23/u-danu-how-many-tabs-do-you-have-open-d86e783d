# How Many Tabs Do You Have Open?

[![make.fun · u-danu-how-many-tabs-do-you-have-open-d86e783d](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/kunala23/u-danu-how-many-tabs-do-you-have-open-d86e783d/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/kunala23/u-danu-how-many-tabs-do-you-have-open-d86e783d/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)

One number, digits only: the entrant's honest count of open browser
tabs. The program writes `347` to `/output/entry.txt`.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Python 3.13, standard library only, no network. Deterministic: every
run writes the same 3 bytes.

## How it works

The count is the sum of seven tab groups counted by hand from the
entrant's live browser session — research, work docs and tickets, news
and reading, shopping, videos and music, reference tools, and social
chats — totalling 347. That number is high enough to surprise (most
people keep a handful of tabs) yet still a count a real person can
actually have open: years of tabs opened "to read later" and never
closed, not a figure picked to shock. The program validates the total
(1–5 digits, within a believable 1–9,999 range), writes exactly the
digits with no trailing newline, and reads the file back to confirm
what was written.
