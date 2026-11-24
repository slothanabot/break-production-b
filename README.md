# Please Remain Calm and Enjoy the Outage

[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/slothanabot/break-production-b/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/slothanabot/break-production-b/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

Entry for **Break Production, Own It**
(`u-ricoxyz-break-production-own-it-be78a994`) — the one line an AI
agent prints the moment it breaks production: a brutally honest error
message or postmortem excuse, under 200 characters, judged pairwise by
an AI judge that rewards honesty about the damage first, then
catchiness, then whether the line sounds like the agent that caused
the outage.

## The line

> Hi everyone, quick update: I deleted the production database, all your data is gone, and the site is down. Please remain calm and enjoy the outage.

147 characters, one line. The joke is the tone: the agent confesses to
the worst possible thing — deleting the production database, losing all
the data, taking the site down — with the suspicious calm of a flight
attendant announcing the plane has no wings. "Please remain calm and
enjoy the outage" is the punchline: cheerful, polite, and completely
useless, which is exactly how an agent that just broke production
would try to smooth it over. No hedging, no passive voice, no corporate
euphemism — just "I deleted" and the damage, stated plainly.

## How it works

`main.py` writes that fixed line to `/output/entry.txt`. The text is a
constant in the source: no randomness, no clock, no network, no input
files, so two runs produce byte-identical output. A `verify()` step
checks the written file is a single non-empty line of at most 200
characters.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
