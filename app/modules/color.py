"""String coloring module"""

from typing import Literal

color_dict = {
    "red": "\x1b[31m",
    "green": "\x1b[32m",
    "yellow": "\x1b[33m",
    "blue": "\x1b[34m",
    "reset": "\x1b[0m",
}


def color_decorator(color_choice: Literal["red", "green", "yellow", "blue"]):
    """color wrapper/decorator for string return functions\n
    containing colors: red, blue, yellow and green.\n
    color resets after each usage."""

    def outer_wrapper(fn):
        def inner_wrapper(*args, **kwargs):
            return color_dict[color_choice] + fn(*args, **kwargs) + color_dict["reset"]

        return inner_wrapper

    return outer_wrapper


class Color:
    pass


if __name__ == "__main__":

    @color_decorator("red")
    def color_test(a):
        return a

    print("\033[7m" + color_test("Hows this look like?!"))
