from time import sleep, time


def stylus_cursor(
    duration: int,
    sleep_interval: float = 0.1,
    cursor_spacing: int = 0,
    shapes: list[str] = ["-", "\\", "|", "/"],
    start_index: int = 0,
    end_print: str = "",
):
    # checkpoint
    end_checkpoint_time = time() + duration

    for i in range(int(duration // sleep_interval) + 1):
        sleep(sleep_interval)
        print(f"{' ' * cursor_spacing}{shapes[start_index]}", end="\r")
        start_index = (i + 1) % 4
        # checkpoint
        if time() > end_checkpoint_time:
            break

    print(end=end_print)


if __name__ == "__main__":
    end = 10
    stylus_cursor(end, cursor_spacing=2)
