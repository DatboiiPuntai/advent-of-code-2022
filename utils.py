def read_input(day: int, test=False):
    if test:
        with open(f"tests/day{day:02d}.txt") as f:
            return f.read()
    else:
        with open(f"data/day{day:02d}.txt") as f:
            return f.read()