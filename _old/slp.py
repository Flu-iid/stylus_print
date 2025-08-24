from time import sleep
import os


class Slp:
    """
    Single Line Printer\n
    print your text with fashionable cursor.
    cursors are single charecter.
    """

    def __init__(self, delimiter: float = 0.2, delay_time: float = 1):
        self.delimiter = delimiter
        self.delay_time = delay_time

    def __str__(self):
        print("<slp Object> current shape: ", end="")
        return self.s

    def choose_shape(self, cursor_line: str = "", shapes=[], index: int = 0) -> None:
        """
        design the cursot here\n
        0: "/"\t
        1: "█"\t
        2: "⚯"\n
        cursor_line defines what should be next to cursor.\n
        default is empty string\n
        shapes is extra option for designing your cursor\n
        shapes accepts sequences
        """
        shape_dict = {
            0: ["|", "/", "-", "\\"],
            1: ["█", " "],
            2: ["⚬", "⚭", "⚮", "⚯", "⚮", "⚭", "⚬"],
        }
        if shapes:
            self.__shapes__ = list(shapes)
        else:
            try:
                self.__shapes__ = shape_dict[index]
            except:
                print("index out of range. using default value")
                self.__shapes__ = shape_dict[0]
        self.s = self.__shapes__[0] + cursor_line

    def next_shape(self) -> str:
        current_shape = self.s[0]
        next_shape = self.__shapes__[
            (self.__shapes__.index(current_shape) + 1) % len(self.__shapes__)
        ]
        self.s = next_shape + self.s[1:]
        return self.s

    # fix same shape bugs, with finding index. probably have to use decorator

    def single_line_printer(self, line: str) -> None:
        all_time = self.delay_time + len(line) * self.delimiter
        current_string = self.s + " "
        while all_time > 0:
            current_string = Slp.next_shape()
            current_string += line[0] if line else ""
            line = line[1:]
            print(current_string, end="\r")
            sleep(self.delimiter)
            all_time -= self.delimiter
        return

    def empty_cursor(self, total_time: int = 2):
        while total_time + self.delay_time > 0:
            print(self.s, end="\r")
            sleep(self.delimiter)
            total_time -= self.delimiter
            self.next_shape()
        return


if __name__ == "__main__":
    o = Slp(delimiter=0.3)
    o.choose_shape(" Hello there", index=2)
    print(o.__shapes__)
    o.empty_cursor(total_time=5)

    # add support for double charecter cursor
