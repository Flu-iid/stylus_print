# Color

also there will be a `color_decorator` which is a simple decorator wrapping the text around ansi representations of

Color will be an object that can be specified for each of the modules.

it will consist of below arguments:

- `color_choice` (`str | None`): specify color representation from basic choices of ["red", "green", "yellow", "blue", "none"].

- `color_code` (`str | None`): specify ansi string color representation to be added to text. if given value it will override `color_choice` value.

- `color_style` (`str | None`): coloring style for each iteration of the object. choices are ["all", "rainbow", "rainbow-char"]. if needed more midfication for coloring you can give function as keyword argument to `color_func`.

- `color_func` (`function | None`): Specify if you need specific coloring function for each iteration at higher level modules.
