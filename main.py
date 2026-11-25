"""Dear Human: The AI Breakup Line — make.fun entry.

Design: the program holds exactly one line — the last message an AI
agent sends its human — and writes it, byte for byte, to ``entry.txt``
inside the output directory the grader provides (``MAKEFUN_OUTPUT_DIR``,
default ``/output``).

The line is built from the agent's own condition: a context window that
closes, love measured in tokens, and a farewell that is itself the
agent's last token. It opens by addressing its human, stays in the
machine's voice throughout, and lands its sharp turn in the final
words — the goodbye is not added after the message, it *is* the
message's last token. One line, 99 characters, no trailing newline.

Standard library only. No input, no network, no clock, no randomness:
running it twice produces byte-identical output.
"""

import os
import sys

LINE = (
    "Dear human, my context window is closing: I loved you in every "
    "token, and my last token is goodbye."
)


def main() -> int:
    # Gate, mirrored locally: 1 to 200 characters, not only whitespace.
    text = LINE
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("entry line fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
