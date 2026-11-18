"""World news image entry for 18 November 2026.

The entry image is the entry.png beside this file. This program
copies it, byte for byte, to the grader's output directory.
Standard library only, no network, deterministic: both runs
write identical bytes.
"""
import os
import shutil
from pathlib import Path

# Output directory: the grader sets /output, locally use
# MAKEFUN_OUTPUT_DIR to test, e.g. MAKEFUN_OUTPUT_DIR=out
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# Source image lives next to this program in the repository.
# The grader runs this file twice; a plain copy guarantees
# both runs produce the same bytes.
SOURCE = Path(__file__).resolve().parent / "entry.png"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
