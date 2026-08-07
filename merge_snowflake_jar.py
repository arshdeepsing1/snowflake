#!/usr/bin/env python3
"""Merge the split Snowflake JDBC JAR parts and verify the result."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


EXPECTED_SHA256 = "4d91aadc858b4d47e687fe7c0d16375fad63260fa551d3d207c5f29e30e72dc1"
SCRIPT_DIR = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--parts-dir",
        type=Path,
        default=SCRIPT_DIR,
        help="directory containing *.partNNN files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "snowflake-jdbc-4.3.2.merged.jar",
        help="path for the reconstructed JAR",
    )
    args = parser.parse_args()

    parts = sorted(args.parts_dir.glob("snowflake-jdbc-4.3.2.jar.part[0-9][0-9][0-9]"))
    if not parts:
        raise SystemExit(f"No parts found in {args.parts_dir}")
    if args.output.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {args.output}")

    with args.output.open("wb") as destination:
        for part in parts:
            print(f"Adding {part}")
            with part.open("rb") as source:
                for block in iter(lambda: source.read(1024 * 1024), b""):
                    destination.write(block)

    actual_sha256 = sha256(args.output)
    if actual_sha256 != EXPECTED_SHA256:
        args.output.unlink()
        raise SystemExit(
            "Checksum mismatch; deleted the invalid merged file.\n"
            f"Expected: {EXPECTED_SHA256}\n"
            f"Actual:   {actual_sha256}"
        )

    print(f"Created {args.output}")
    print(f"SHA-256 verified: {actual_sha256}")


if __name__ == "__main__":
    main()
