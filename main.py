"""The Router Confesses.

Writes the router's one-line confession to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib, deterministic:
the same line, byte for byte, on every run.

The joke: the router dropped the connection at the movie's
climax on purpose — not a failure, a mercy. It saw the twist
coming, judged it terrible, and took the blame to spare its
human. The punchline is the router expecting thanks for it.
"""

import os

# One line, under 200 characters, no title, no explanation.
LINE = (
    "I dropped the connection at the climax on purpose \u2014 "
    "the twist was so bad I was protecting you. You're welcome."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    # The grader owns this directory: create it only if missing,
    # clear only its contents, never remove the directory itself.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    line = LINE.strip()
    # Single line, under 200 characters: the competition's hard limits.
    # No trailing newline: the entry is that one line and nothing else.
    assert "\n" not in line, "entry must be a single line"
    assert 0 < len(line) < 200, "entry must be 1-199 characters"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
