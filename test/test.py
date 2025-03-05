from time import sleep

shapes: list[str] = ["-", "\\", "|", "/"]
i = 0

while True:
    sleep(0.1)
    print(f"{shapes[i]}", end="\r")
    i = (i + 1) % 4
