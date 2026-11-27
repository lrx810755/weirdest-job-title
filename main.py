"""make.fun entry: Weirdest Job Title.

Writes one job title, 39 characters, to entry.txt.
"""

import os
from pathlib import Path

# One job title, 39 characters, within the 60 character limit.
LINE = "Senior Apologizer for Self-Driving Cars"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
