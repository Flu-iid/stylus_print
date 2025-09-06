"""Coloring module"""

from typing import Literal, Callable


def color_decorator(
    color_choice: Literal["red", "green", "yellow", "blue", "none"] = "red",
) -> Callable[..., Callable[..., str]]:
    """color wrapper/decorator for string return functions\n
    containing colors: red, blue, yellow and green.\n
    color resets after each usage."""

    def outer_wrapper(fn) -> Callable[..., str]:
        def inner_wrapper(*args, **kwargs) -> str:
            return (
                Color.color_dict[color_choice] + fn(*args, **kwargs) + Color.color_clear
            )

        return inner_wrapper

    return outer_wrapper


class Color:
    """Class for modifying text color representation.\n"""

    color_dict: dict[str, str] = {
        "red": "\x1b[31m",
        "green": "\x1b[32m",
        "yellow": "\x1b[33m",
        "blue": "\x1b[34m",
        "none": "\x1b[0m",
    }

    color_clear: str = "\x1b[0m"

    color_names = list(color_dict.keys())
    color_styles: list[str] = ["all", "rainbow", "rainbow-char"]

    def __init__(
        self,
        color_choice: Literal["red", "green", "yellow", "blue", "none"] | None = None,
        color_code: str | None = None,
        color_style: Literal["all", "rainbow", "rainbow-char"] = "all",
        color_func: Callable | None = None,
    ) -> None:
        self.color_choice: str = color_code if color_code else color_choice or "none"
        self.color_mapped_fn: list[Callable[[str], str]] = [
            self._all,
            self._rainbow,
            self._rainbow_char,
        ]  # mapped fn
        self.color_map = dict(zip(self.color_styles, self.color_mapped_fn))
        self.color_style = color_func or self._choose_style(color_style)
        # self.next_color_index = 0  # for one by one char func

    def _all(self, text: str) -> str:
        """Changing colors of all charecters"""
        # self.color_style = "all"
        return self.color_dict[self.color_choice] + text + self.color_dict["none"]

    def _rainbow(self, text, index: int = 0) -> str:
        """Applying sequence of colors to each charecter of text"""
        # self.color_style = "rainbow"
        color_count = len(self.color_names)
        colored_list = []
        for c in text:
            colored_list.append(self.color_dict[self.color_names[index]] + c)
            index = (index + 1) % color_count
        return "".join(colored_list)

    def _rainbow_char(self, char: str, color_index: int = 0) -> tuple[str, int]:
        """Applying color for one charecter. returning modifed charecter and next color_index"""
        # self.color_style = "rainbow-char"
        color_count = len(self.color_names)
        self.next_color_index = (color_index + 1) % color_count
        return self.color_dict[
            self.color_names[color_index]
        ] + char, self.next_color_index

    def _choose_style(
        self,
        color_style: Literal["all", "rainbow", "rainbow-char"] | None = None,
    ) -> None:
        color_style = color_style or self.color_style
        if color_style not in self.color_styles:
            pass
            # raise error, wrong style
        else:
            self.paint = self.color_map[color_style]
        return color_style


if __name__ == "__main__":

    @color_decorator("red")
    def color_test(a):
        return a

    print("\033[7m" + color_test("Hows this look like?!"))

    my_color = Color(color_style="rainbow")
    test_result = my_color.paint("hello world")
    print(test_result)
