#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261120.

Copies the bundled front-page image (entry.png, 1024x1024, built for
Friday, 20 November 2026) into the output directory and verifies the copy.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable and defaults to /output. No relative paths are used: the source
image is resolved against this file's own directory, and the destination
is always absolute.
"""

import binascii
import hashlib
import os
import shutil
import struct
import sys

EXPECTED_SHA256 = "d258ffd83dff9118757d2c9dffaadc996298f72dcba33fe24d1e4ffe8b5c3ba7"
EXPECTED_SIZE = 875744
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1048576


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_dir = os.path.abspath(out_dir)
    dest = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(source):
        return fail("bundled image not found: " + source)

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, dest)

    with open(dest, "rb") as fh:
        data = fh.read()

    if len(data) != EXPECTED_SIZE:
        return fail("size mismatch: got %d bytes, expected %d"
                    % (len(data), EXPECTED_SIZE))
    if len(data) > MAX_BYTES:
        return fail("image exceeds 1 MiB: %d bytes" % len(data))
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return fail("not a PNG file")
    if len(data) < 33 or data[12:16] != b"IHDR":
        return fail("missing PNG IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        return fail("dimensions mismatch: got %dx%d, expected %dx%d"
                    % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT))
    # The file must be whole: every chunk checksummed, ending in IEND.
    ihdr_crc = struct.unpack(">I", data[29:33])[0]
    if binascii.crc32(data[12:29]) & 0xFFFFFFFF != ihdr_crc:
        return fail("IHDR chunk checksum mismatch")
    if data[-12:] != struct.pack(">I", 0) + b"IEND" + struct.pack(
            ">I", binascii.crc32(b"IEND") & 0xFFFFFFFF):
        return fail("missing PNG IEND terminator")
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        return fail("sha256 mismatch: got " + digest)

    print("wrote %s (%d bytes, %dx%d, sha256 %s)"
          % (dest, len(data), width, height, digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
