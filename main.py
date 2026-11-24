"""Dad Joke Showdown entry: one original dad joke, written to /output/entry.txt.

Deterministic, stdlib only, no network. The joke is embedded below and is
written byte-for-byte on every run.
"""

import os

JOKE = "My son asked why my band is called 'The Potatoes.' I said, 'Because we mash well together.'"
# The pun: potatoes mash, bandmates mesh — "mash well together" turns on
# hearing one word as the other, delivered straight-faced at the table.

OUT = "/output/entry.txt"


def main():
    assert 1 <= len(JOKE) <= 200, "joke must be 1 to 200 characters"
    assert JOKE.strip(), "joke must not be only white space"
    try:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        out_path = OUT
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(JOKE)
    except OSError:
        # Local fallback only: the grader's /output is writable, so this
        # path must never trigger there.
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "output", "entry.txt")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(JOKE)
    print("wrote", out_path, "({} characters)".format(len(JOKE)))


if __name__ == "__main__":
    main()
