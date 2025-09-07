"""Coloring module"""

from typing import Literal, Callable, Optional, Any
from inspect import Signature, signature


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
    """Class for modifying text color representation.\n
    Key parameters:\n
    1. color_choice\n
        support (red, green, yellow, blue, none) Literals\n
    2. color_code\n
        custome ansi code for coloring. overwrites color_choice\n
    3. color_style\n
        default coloring styles (all, rainbow)\n
    4. color_func\n
        custome function for styling (support lambda)\n
        [index_condition, char_condition = True] (can have 1 or 2 parameters. 2nd one is optional)\n"""

    color_dict: dict[str, str] = {
        "red": "\x1b[31m",
        "green": "\x1b[32m",
        "yellow": "\x1b[33m",
        "blue": "\x1b[34m",
        "none": "\x1b[0m",
    }

    color_clear: str = "\x1b[0m"

    color_names = list(color_dict.keys())
    color_styles: list[str] = ["all", "rainbow"]

    def __init__(
        self,
        color_choice: Literal["red", "green", "yellow", "blue", "none"] | None = None,
        color_code: Optional[str] = None,
        color_style: Literal["all", "rainbow"] = "all",
        color_func: Optional[Callable] = None,
    ) -> None:
        self.color_choice: str = color_code or color_choice or "none"
        self.color_mapped_fn: list[Callable[[str], str]] = [
            self._all,
            self._rainbow,
        ]  # mapped fn
        self.color_map = dict(zip(self.color_styles, self.color_mapped_fn))
        self.paint: Callable[..., Any] = self._custome_func(
            color_func
        ) or self._choose_style(color_style)
        # self.next_color_index = 0  # for one by one char func
        # self.paint: Callable[[str], str] = None

    def _all(self, text: str) -> str:
        """Changing colors of all charecters"""
        # self.color_style = "all"
        return self.color_dict[self.color_choice] + text + self.color_dict["none"]

    def _rainbow(self, text: str, index: int = 0) -> str:
        """Applying sequence of colors to each charecter of text"""
        # self.color_style = "rainbow"
        color_count: int = len(self.color_names)
        colored_list: list = []
        for c in text:
            colored_list.append(self.color_dict[self.color_names[index]] + c)
            index = (index + 1) % color_count
        colored_list.append(self.color_clear)
        return "".join(colored_list)

    def _custome_func(self, fn: Callable[[Any], str] | None = None) -> str:
        """Customized function in place of default ones, with focus on functioning with lamda functions."""
        if not fn:
            return False
        else:
            lambda_sig: Signature = signature(fn)
            lambda_parameter_len = len(lambda_sig.parameters)

            def fn_wrapper(text: str) -> str:
                colored_list: list = []
                for i, c in enumerate(text):
                    match lambda_parameter_len:
                        case 1:
                            lambda_condition: Any = fn(i)
                        case 2:
                            lambda_condition: Any = fn(i, c)
                        case _:
                            # raise error
                            pass
                    if lambda_condition:
                        colored_list.append(
                            self.color_dict[self.color_choice] + c + self.color_clear
                        )
                    else:
                        colored_list.append(c)

                return "".join(colored_list)

        return fn_wrapper

    def _choose_style(
        self,
        color_style: Literal["all", "rainbow"] | None = None,
    ) -> None:
        if color_style not in self.color_styles:
            pass
            # raise error, wrong style
        return self.color_map[color_style]


if __name__ == "__main__":

    @color_decorator("red")
    def color_test(a):
        return a

    print("\033[7m" + color_test("Hows this look like?!"))

    my_color = Color(color_style="rainbow")
    test_result = my_color.paint("hello world")
    print(test_result)

    my_color = Color(color_choice="blue", color_func=lambda i, c: i == 0 and c == "A")
    test_result_2 = my_color.paint("Arsham")
    print(test_result_2)
