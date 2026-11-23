import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "assets" / "entry.png"
OUTPUT = Path("/output/entry.png")


def main() -> int:
    source = SOURCE
    if not source.is_file():
        print(f"missing source image: {source}", file=sys.stderr)
        return 1

    data = source.read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        print(f"invalid PNG source: {source}", file=sys.stderr)
        return 1

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
