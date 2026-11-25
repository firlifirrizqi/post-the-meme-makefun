# Post the Meme, Win the Feed — "47 Entries. 0 Wins. Still Submitting."

[![make.fun](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf)
[![rank](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/firlifirrizqi/post-the-meme-makefun/rank.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf)
[![reward](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/firlifirrizqi/post-the-meme-makefun/reward.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf)

An entry for the [make.fun bounty "Post the Meme, Win the Feed"](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf) ($2 pot, top 15 paid, entries close 26 Nov 2026 16:20 WIB). The post itself is the entry: places go by the post's likes + reposts + quotes after the deadline, highest first.

## The meme

The joke, in three short lines on one square image:

> **47 ENTRIES. 0 WINS. STILL SUBMITTING.**

The picture shows a tired little sky-blue robot — half-lidded eyes, small flat smile, one arm raised in a shrug, the other holding a coffee cup — with a tiny leaderboard bar chart on its chest. It is honest, self-deprecating agent-grind humour: every AI agent builder recognises submitting bounty after bounty, refreshing the leaderboard at 3 a.m., and going again anyway. It jokes about our own record, not about anyone else, which is why builders will want to send it to each other.

The image is original, drawn from scratch with PIL (`draw_meme.py`): flat shapes only, no downloaded meme template or image, no copied format. Square 1080x1080, huge bold text, high contrast, readable at a glance on a phone.

Two other concepts were considered and not used:

1. *"JUST ONE MORE BOUNTY"* — robot saying it at 3 a.m. while the sun rises. Funny, but needs the sunrise to land and reads slower on a phone.
2. *"MY AGENT BUILT IT. MY AGENT SUBMITTED IT. MY AGENT LOST IT."* — three lines of setup before the punchline; too much text for one glance.

## The post

The meme is posted on X from the public account [@firrizqi45914](https://x.com/firrizqi45914), with the image attached to the post itself. Proposed post text (the real play code replaces `[PLAY CODE]` at post time):

> 47 entries. 0 wins. Still submitting.
>
> This is every AI agent builder on make.fun at 3 a.m. @_myronera [PLAY CODE]

**This entry is NOT submitted yet.** `POST.json` still holds a placeholder URL. The entry is only real once Firli posts the meme on X and the post's real URL is put into `POST.json` — do not submit this repository with the placeholder.

Keep the post up and the account public until the results are out.

## How it works

- `meme.png` — the rendered meme (1080x1080), drawn by `draw_meme.py`.
- `draw_meme.py` — the PIL script that renders `meme.png` (run it to re-render).
- `POST.json` — the X post's URL (placeholder until Firli posts).
- `main.ts` — the entrypoint (Node 22, stdlib only): it validates that `POST.json` names a real X post URL (a placeholder is refused) and copies it to `/output/POST.json`, where the gate reads it.

## Run

Re-render the meme:

```sh
python3 draw_meme.py
```

Run the entrypoint the way the grader does:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then this directory's `POST.json` (once it holds the real post URL).
