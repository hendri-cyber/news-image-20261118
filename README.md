# Sum up 18 November's world news in one image

Entry for make.fun bounty `news-image-20261118` — $250, 50 places paid,
ends Fri 20 Nov 2026 00:00 UTC.

## What it shows

Wednesday, 18 November 2026:

- **Hero — Gulf escalation:** U.S. jets struck a Revolutionary Guard
  missile site on Qeshm Island; Iran answered with drones and missiles
  at U.S. bases in Kuwait and Bahrain.
- **Kerch Bridge:** Ukraine hit the bridge to Crimea; a road arch fell
  into the strait, traffic halted.
- **APEC, Shenzhen:** Xi vows to fight protectionism; Putin attacks
  sanctions, ahead of a Trump meeting.
- **U.S. Senate:** Mary Peltola wins Alaska; Democrats take a 56–44
  majority.
- **Health:** Ebola outbreak in DR Congo passes 11,000 cases.
- **Also today:** Voyager 1 reaches one light-day from Earth;
  U.S. loses measles-free status after 26 years.

Sources: Reuters, NASA, UN — 18 Nov 2026.

## How it works

`main.py` is standard library only. It copies `entry.png` (1024×1024,
124 KB) to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR` locally).
Both runs write identical bytes. No network.

Test locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see LICENSE.
