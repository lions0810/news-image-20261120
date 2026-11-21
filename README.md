[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/lions0810/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/lions0810/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World in One Page — Friday, 20 November 2026

Entry for the [make.fun bounty "Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120) ($250, top 50 share).

## The image

A 1024×1024 newspaper front page summing up Friday, 20 November 2026, researched from that day's wire reporting:

- **Lead — Missiles fall on Poland.** Two Russian missiles and a suspected drone come down in Poland; Warsaw calls it a deliberate provocation, NATO a grave violation of allied airspace.
- **World Court: Myanmar guilty of genocide.** The ICJ rules 9–6 that Myanmar's forces committed genocide against the Rohingya in Rakhine State.
- **The AI rally unravels.** The S&P 500 falls 3.7% into correction and the Nikkei drops 5.1% as AI shares sell off worldwide.
- **Three powers, no breakthrough.** Trump, Xi and Putin meet for 70 minutes in Shenzhen and issue a joint peace declaration — but no deal on Ukraine, Iran or arms limits.
- **Kyiv hit again overnight.** Russia's missile and drone attack kills seven in Kyiv and knocks out a power plant; Kryvyi Rih is also struck.
- **Also today:** a Houthi missile hits Riyadh's PIF Tower; Britain and the EU sign food, carbon and youth-mobility deals; Cyclone Akvan makes landfall in Odisha; a magnitude 6.7 earthquake strikes central Peru; BepiColombo reaches Mercury after eight years; the US loses measles elimination status; a jury convicts the Palisades Fire arsonist; Anthropic shares slide after a record IPO; the Senate passes an energy-permitting bill 62–33; COP31 wraps up.

The five panels are original illustrations generated for this entry; all headlines, decks and the "Also today" list were written from the day's reporting and typeset in this build. No text is garbled: every word on the page is set by code, not by an image model.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled `entry.png` into the output directory and verifies the copy before exiting:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 -P -s main.py
```

- The output directory comes from `MAKEFUN_OUTPUT_DIR` (default `/output`); no relative paths are used.
- The copy is verified: PNG signature, 1024×1024 dimensions, size ≤ 1 MiB, and sha256 match against the hash recorded in `main.py`.
- The program is deterministic: every run writes the same bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the front-page image (1024×1024, 875,744 bytes)
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
