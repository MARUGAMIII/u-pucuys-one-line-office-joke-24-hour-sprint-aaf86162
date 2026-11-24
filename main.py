"""One-line office joke entry.

Writes a single-line joke about office life to /output/entry.txt.
The text must be plain ASCII, one line, 1-200 characters.
"""

JOKE = "I told the printer it was out of paper, so it printed a 40-page error report about being out of paper."


def main():
    text = JOKE.strip()
    # Gate self-check: mirror the sealed scorer (1-200 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
