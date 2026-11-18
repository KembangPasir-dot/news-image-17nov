"""Copy the bundled entry.png to /output/entry.png."""

import hashlib
import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"

BASE_DIR = Path(__file__).resolve().parent
SRC = BASE_DIR / IMAGE_NAME


def main() -> None:
    out_dir = (BASE_DIR / os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / IMAGE_NAME
    shutil.copyfile(SRC, destination)

    size = SRC.stat().st_size
    if not destination.is_file() or destination.stat().st_size != size:
        raise RuntimeError("Copied PNG is missing or has the wrong size")

    digest = hashlib.sha256(SRC.read_bytes()).hexdigest()
    if hashlib.sha256(destination.read_bytes()).hexdigest() != digest:
        raise RuntimeError("Copied PNG has the wrong SHA-256")

    print(f"{IMAGE_NAME}: {size} bytes, sha256={digest}")


if __name__ == "__main__":
    main()
