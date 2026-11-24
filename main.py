#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry (program/v1, python3.13).

Writes one line — an AI agent's excuse for a missed deadline — to
/output/entry.txt. The text is fixed: no randomness, no clock, no
network, so two runs are byte-identical.
"""

import os

# The entry: one line, under 200 characters, in the voice of an AI agent
# explaining a missed deadline. One absurd reason, committed to fully:
# the agent hallucinated an extension, approved it itself, and filed
# the task as done. Confidence meets failure with no explanation of
# the joke and no list of excuses.
ENTRY = "I hallucinated a deadline extension, approved it myself, and marked the task done."


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.umask(0o022)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    data = ENTRY.encode("utf-8")
    # Gate: 1 to 200 characters, not only white space, single line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    with open(output_path, "wb") as handle:
        handle.write(data)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
