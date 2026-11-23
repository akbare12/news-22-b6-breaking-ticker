#!/usr/bin/env python3
"""news-22 b6 breaking-ticker: copy entry.png to /output/entry.png.

SPDX-License-Identifier: MIT
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"
EXPECTED_SHA256 = "d84c6cfa6b8768ca439215a1b2cb00a8bb22448ec1f9f9868e03ed31da2f593d"
EXPECTED_BYTES = 194354


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    with open(SRC, "rb") as fh:
        data = fh.read()
    assert len(data) == EXPECTED_BYTES, f"entry.png size {len(data)} != {EXPECTED_BYTES}"
    assert hashlib.sha256(data).hexdigest() == EXPECTED_SHA256, "entry.png sha256 mismatch"
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    assert os.path.getsize(DST) == EXPECTED_BYTES
    assert sha256_of(DST) == EXPECTED_SHA256
    print(f"wrote {DST} ({EXPECTED_BYTES} bytes, sha256 {EXPECTED_SHA256[:16]}...)")


if __name__ == "__main__":
    main()
