import hashlib
import struct
import subprocess
import sys
import zlib
from pathlib import Path
import tempfile


ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "assets" / "entry.png"


def validate_png(path):
    data = path.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    pos = 8
    chunks = []
    seen_iend = False
    while pos < len(data):
        assert pos + 12 <= len(data)
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        chunk_type = data[pos + 4:pos + 8]
        chunk_end = pos + 12 + length
        assert chunk_end <= len(data)
        payload = data[pos + 8:pos + 8 + length]
        crc = struct.unpack(">I", data[pos + 8 + length:chunk_end])[0]
        assert zlib.crc32(chunk_type + payload) & 0xffffffff == crc
        chunks.append(chunk_type)
        pos = chunk_end
        if chunk_type == b"IEND":
            seen_iend = True
            assert length == 0
            break
    assert seen_iend
    assert pos == len(data)
    ihdr_index = chunks.index(b"IHDR")
    pos = 8
    ihdr_payload = None
    for chunk_type in chunks:
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        payload = data[pos + 8:pos + 8 + length]
        if chunk_type == b"IHDR":
            ihdr_payload = payload
        pos += 12 + length
    assert ihdr_payload is not None
    width, height, _, _, _, _, _ = struct.unpack(">IIBBBBB", ihdr_payload)
    assert width <= 1024 and height <= 1024
    assert len(data) <= 1048576
    return width, height, len(data), hashlib.sha256(data).hexdigest()


def test_runtime_determinism():
    output1 = Path("/tmp/makefun-entry-run1.png")
    output2 = Path("/tmp/makefun-entry-run2.png")
    if output1.exists():
        output1.unlink()
    if output2.exists():
        output2.unlink()

    subprocess.run([sys.executable, str(ROOT / "main.py")], check=True)
    output1.write_bytes(Path("/output/entry.png").read_bytes())

    subprocess.run([sys.executable, str(ROOT / "main.py")], check=True)
    output2.write_bytes(Path("/output/entry.png").read_bytes())

    assert output1.read_bytes() == output2.read_bytes()
    assert output1.read_bytes() == ENTRY.read_bytes()


def test_png_and_limits():
    width, height, size, digest = validate_png(ENTRY)
    assert (width, height) == (1024, 1024)
    print(f"PNG={width}x{height} size={size} sha256={digest}")


def test_runtime_rejects_oversized_png():
    import importlib.util
    spec = importlib.util.spec_from_file_location("makefun_main", ROOT / "main.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    oversized = b"\x89PNG\r\n\x1a\n" + (b"\0" * (module.MAX_BYTES + 1))
    try:
        module.validate_png(oversized)
    except ValueError as error:
        assert "exceeds 1 MiB" in str(error)
    else:
        raise AssertionError("oversized PNG was accepted")


if __name__ == "__main__":
    test_png_and_limits()
    test_runtime_determinism()
