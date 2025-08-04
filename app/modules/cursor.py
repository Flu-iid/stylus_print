from time import sleep, time
from typing import Literal, Optional
from app.modules.color import color_dict


class Cursor:
    sequence_default_dict = {
        0: ["|", "/", "-", "\\"],
        1: ["█", " "],
        2: ["⚬", "⚭", "⚮", "⚯", "⚮", "⚭", "⚬"],
        3: ["■", "□", "▪", "▫"],
        4: ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"],
    }

    def __init__(
        self,
        sequence: Optional[list[str]] = None,
        interval: float = 0.1,
        position: Literal["leading", "trailing", "below"] = "trailing",
        blink_mode: Literal["always", "during_print", "post_print"] = "always",
        color: Optional[str] = None,  # make Color obj
        offset: int = 0,
        reset_after: bool = True,  # hide after animation
    ) -> None:
        pass
