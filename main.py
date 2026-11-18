"""Deliver the 18 November 2026 world-news image to the grader.

The picture lives beside this script. The script copies it,
byte for byte, into the grader's output folder. It needs no
network, no clock and no randomness, so running it twice
produces the same file twice.
"""

import os
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent
PICTURE = BASE / "entry.png"
OUTDIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTDIR / "entry.png"


def main() -> None:
    """Copy the picture into the grader's output folder."""
    OUTDIR.mkdir(parents=True, exist_ok=True)
    if not PICTURE.is_file():
        raise SystemExit(f"entry image missing: {PICTURE}")
    shutil.copyfile(PICTURE, TARGET)
    got = TARGET.stat().st_size
    want = PICTURE.stat().st_size
    if got != want:
        raise SystemExit(f"incomplete copy, got {got} bytes, expected {want}")


if __name__ == "__main__":
    main()
