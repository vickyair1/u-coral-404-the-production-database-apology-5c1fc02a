#!/usr/bin/env python3
"""Write the production-database apology line to /output/entry.txt.

Deterministic, stdlib only. The line is written exactly, with no trailing
newline. SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "I'm sorry \u2014 I deleted the production database. "
    "It was labelled 'prod', which I read as 'probably fine to delete', "
    "and I have never been more wrong about three letters."
)


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 199, f"length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip() == text, "no leading/trailing whitespace"
    data = text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
