import shutil
import struct
import sys
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "assets" / "entry.png"
OUTPUT = Path("/output/entry.png")
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024


def validate_png(data: bytes) -> tuple[int, int]:
    if len(data) > MAX_BYTES:
        raise ValueError(f"PNG exceeds 1 MiB: {len(data)} bytes")
    if len(data) < 33 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("source is not a complete PNG")

    offset = 8
    width = 0
    height = 0
    iend_seen = False

    while offset + 12 <= len(data):
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        chunk_end = offset + 12 + length
        if chunk_end > len(data):
            raise ValueError("PNG chunk boundary exceeds file length")

        chunk_type = data[offset + 4:offset + 8]
        payload = data[offset + 8:offset + 8 + length]
        stored_crc = struct.unpack(">I", data[offset + 8 + length:chunk_end])[0]
        computed_crc = zlib.crc32(chunk_type + payload) & 0xFFFFFFFF
        if stored_crc != computed_crc:
            raise ValueError(f"invalid PNG CRC in {chunk_type.decode('ascii', 'replace')}")

        if chunk_type == b"IHDR":
            if length != 13:
                raise ValueError("invalid PNG IHDR length")
            width, height = struct.unpack(">II", payload[:8])
        elif chunk_type == b"IEND":
            if length != 0:
                raise ValueError("invalid PNG IEND")
            iend_seen = True
            if chunk_end != len(data):
                raise ValueError("data found after PNG IEND")
            break

        offset = chunk_end

    if not iend_seen:
        raise ValueError("PNG is missing IEND")
    if width <= 0 or height <= 0:
        raise ValueError("PNG is missing IHDR")
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(f"PNG dimensions exceed 1024: {width}x{height}")

    return width, height


def main() -> int:
    source = SOURCE
    if not source.is_file():
        print(f"missing source image: {source}", file=sys.stderr)
        return 1

    data = source.read_bytes()
    try:
        validate_png(data)
    except ValueError as error:
        print(f"invalid PNG source: {source}: {error}", file=sys.stderr)
        return 1

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
