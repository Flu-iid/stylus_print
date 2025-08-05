"""Cursor module"""

from time import sleep
from typing import Literal, Optional
from color import Color


class Cursor:
    """Class representation of Cursor\n
    default sequences:
        0: "|"
        1: "█"
        2: "⚬"
        3: "■"
        4: "⣾"
        5: "⠁"
    """

    sequence_default_dict = {
        0: ["|", "/", "-", "\\"],
        1: ["█", " "],
        2: ["⚬", "⚭", "⚮", "⚯", "⚮", "⚭", "⚬"],
        3: ["■", "□", "▪", "▫"],
        4: ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"],
        5: ["⠁", "⠂", "⠄", "⡀", "⢀", "⠠", "⠐", "⠈"],
    }

    def __init__(
        self,
        sequence: Optional[list[str] | int] = None,
        interval: float = 0.1,
        position: Literal["leading", "trailing", "below"] = "trailing",
        blink_mode: Literal["always", "during_print", "post_print"] = "always",
        have_color: bool = False,  # add Color instance to cursor representation
        offset: int = 0,  # cursor offset from text
        stop: bool = False,  # hide after animation
    ) -> None:
        # self.__sequence__ = None
        # self.__shape__ =
        self.add_sequence(sequence)
        self.__interval__ = interval
        self.position = position
        self.blink_mode = blink_mode
        self.cursor_color = Color("red") if have_color else None
        self.offset = offset
        self.stop = stop

    def __str__(self) -> str:
        """String representation of the instance"""
        return f"<Cursor Object> current shape: {self.__shape__}"  # needs fixing

    def add_sequence(self, sequence: Optional[list[str] | int] = None) -> None:
        """
        add or change current sequence by adding new sequence or choose from defualt ones.\n
        default sequences:
        0: "|"
        1: "█"
        2: "⚬"
        3: "■"
        4: "⣾"
        5: "⠁"
        """
        # add right sequence to instance
        sequence = sequence if sequence else self.sequence_default_dict[0]
        try:
            if isinstance(sequence, list):
                self.__sequence__ = sequence
            elif isinstance(sequence, int):
                self.__sequence__ = self.sequence_default_dict[sequence]
            else:
                raise ValueError
        except ValueError:
            print("Bad Sequence input")
        else:
            self.__shape__: list[str, int] = [
                self.__sequence__[0],
                0,
            ]  # shape and index pair list

    def next_shape(self, index: Optional[int] = None) -> str:
        """Selecting next shape from sequence."""
        cur_shape_index = index if isinstance(index, int) else self.__shape__[1]
        n_shape_index = (cur_shape_index + 1) % len(self.__sequence__)
        n_shape = self.__sequence__[n_shape_index]  # next_shape
        if self.cursor_color:
            n_shape, n_color_index = self.cursor_color.rainbow_char(
                n_shape, self.cursor_color.next_color_index
            )
            self.cursor_color.next_color_index = n_color_index
        self.__shape__ = n_shape, n_shape_index
        return n_shape

    def color_config(
        self,
        color_choice: Literal["red", "green", "yellow", "blue", "none"],
        style: Literal["all", "rainbow", "rainbow-char"] = "all",
    ) -> None:
        """Adds color to cursor shapes."""
        self.cursor_color.color_choice = color_choice
        self.cursor_color.color_style = style
        # match style:
        #     case "all":
        #         pass
        #     case "rainbow":
        #         pass
        #     case "rainbow-char":
        #         pass
        #     case _:
        #         raise ValueError  # needs error handling

    def run(self) -> None:
        """Standalone cursor sequence representation."""
        while not self.stop:
            cur_shape = self.__shape__[0]  # current shape
            print(self.offset * " ", cur_shape, sep="", end="\r")
            sleep(self.__interval__)
            cur_shape = self.next_shape()


# fix positioning, blink_mode
# turn shape into class
# add reconfigure module

if __name__ == "__main__":
    my_cursor = Cursor(sequence=3, offset=12, have_color=True)
    my_cursor.run()
    # make self.stop work with async
