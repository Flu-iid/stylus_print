"""Text coloring module"""

from typing import Literal


def color_decorator(color_choice: Literal["red", "green", "yellow", "blue"]):
    """color wrapper/decorator for string return functions\n
    containing colors: red, blue, yellow and green.\n
    color resets after each usage."""

    def outer_wrapper(fn):
        def inner_wrapper(*args, **kwargs):
            return (
                Color.color_dict[color_choice]
                + fn(*args, **kwargs)
                + Color.color_dict["none"]
            )

        return inner_wrapper

    return outer_wrapper


class Color:
    """Class for modifying text color representation."""

    color_dict = {
        "red": "\x1b[31m",
        "green": "\x1b[32m",
        "yellow": "\x1b[33m",
        "blue": "\x1b[34m",
        "none": "\x1b[0m",
    }

    color_names = list(color_dict.keys())

    def __init__(
        self,
        color_choice: Literal["red", "green", "yellow", "blue", "none"] | None = None,
    ) -> None:
        self.__color__ = color_choice if color_choice else "none"

    def all(self, text: str) -> str:
        """Changing colors of all charecters"""
        return self.color_dict[self.__color__] + text + self.color_dict["none"]

    def one_by_one(self, text, index_input: int | None = None) -> str:
        """Applying sequence of colors to each charecter of text"""
        color_count = len(self.color_names)
        cur_i = index_input if index_input else 0
        colored_list = []
        for c in text:
            colored_list.append(
                self.color_dict[self.color_names[cur_i]] + c + self.color_dict["none"]
            )
            cur_i = (cur_i + 1) % color_count
        return "".join(colored_list)


if __name__ == "__main__":

    @color_decorator("red")
    def color_test(a):
        return a

    print("\033[7m" + color_test("Hows this look like?!"))

    my_color = Color()
    test_result = my_color.one_by_one("hello world")
    print(test_result)
