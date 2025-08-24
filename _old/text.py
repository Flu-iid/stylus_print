from time import sleep


def stylus_text(
    text: str,
    interval: float = 0.1,
    ending: str = "\n",
):
    for i, c in enumerate(text):
        sleep(interval)
        print(text[: i + 1], end="\r" if i < len(text) - 1 else ending)


if __name__ == "__main__":
    stylus_text("hello", ending="\r")
