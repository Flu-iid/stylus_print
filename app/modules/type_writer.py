"""Typewriter module"""

from typing import Literal, Optional
from time import sleep
from app.modules.color.color import Color


class TypeWriter:
    """TypeWriter class\n to represent text in animated fashion."""

    def __init__(
        self,
        text: str,
        interval: float = 0.1,
        have_color: bool = False,
        style: Literal[
            "bold", "italic", "underline", "none"
        ] = "none",  # ansi escape for bold, italic, ...
        stop: bool = False,  # stop signal
    ) -> None:
        self._text = text
        self._text_len = len(self._text)
        self._interval = interval
        self.color = (
            Color(color_choice="none", color_style="rainbow-char")
            if have_color
            else None
        )
        self.style = style
        self._stop = stop
        self.__charecter__ = ["", -1]  # char, index

    def next_char(self) -> list[str, int]:
        """Returning next char from text."""
        n_char, n_index = self.__charecter__
        if n_char == self._text_len:
            return None
        n_index += 1
        n_char = self._text[n_index]
        if self.color:
            n_char, n_color_index = self.color.paint(
                n_char, self.color.next_color_index
            )
            self.color.next_color_index = n_color_index
        self.__charecter__ = [n_char, n_index]
        return n_char

    def color_config(
        self,
        color_choice: Literal["red", "green", "yellow", "blue", "none"],
        color_style: Literal["all", "rainbow", "rainbow-char"] = "rainbow-char",
    ):
        """Add color to text charecters."""
        if self.color:
            del self.color

        self.color = Color(color_choice=color_choice)
        self.color.color_style = color_style

    def run(self):
        """Standalone typewriter representation."""
        for i, c in enumerate(self._text):
            if self._stop:
                break
            print(self.next_char(), sep="", end="" if i < self._text_len - 1 else "\n")
            sleep(self._interval)


# can add frame rate to both typewriter and cursor instead of simple interval


if __name__ == "__main__":
    text = "hello world"
    my_type_writer = TypeWriter(text, have_color=True)
    my_type_writer.run()
