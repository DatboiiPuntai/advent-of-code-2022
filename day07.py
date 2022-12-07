from utils import read_input
from pathlib import Path
from collections import defaultdict

ROOT = Path("/")

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000

def parse(input_str: str):
    file_sizes = defaultdict(dict)
    path = ROOT

    for line in input_str.splitlines():
        cmd = line.split()
        if cmd[0] == '$':
            if cmd[1] == 'ls': 
                continue
            path = (path / Path(cmd[2])).resolve()
        else:
            kind, name = cmd
            if kind != 'dir':
                file_sizes[path / name] = int(kind)
    return diskUsage(file_sizes)

def diskUsage(file_sizes: dict[Path, int]):
    directory_sizes = defaultdict(int)
    for path, size in file_sizes.items():
        for parent in path.parents:
            directory_sizes[parent] += size
    return directory_sizes

def main():
    input_str = read_input(day=7)
    directory_sizes = parse(input_str)
    # part 1
    sizeSum = 0
    for size in directory_sizes.values():
        if size <= 100000:
            sizeSum += size
    print(sizeSum)

    # part 2
    free_space = TOTAL_SPACE - directory_sizes[ROOT.resolve()]
    missing_space = REQUIRED_SPACE - free_space
    print(min(size for size in directory_sizes.values() if size >= missing_space))




if __name__ == '__main__':
    main()
