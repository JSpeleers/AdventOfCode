from itertools import groupby

from util.decorators import aoc_timed_solution

FILL = '#'
EMPTY = '.'


def read(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    schemas = [list(map(str.strip, group)) for is_split, group in groupby(lines, lambda x: x == '\n') if not is_split]
    locks, keys = [], []
    for schema in schemas:
        if FILL in schema[0]:
            locks.append(schema)
        else:
            keys.append(schema)
    return locks, keys


def does_fit(lock, key):
    size = len(lock)
    # print(f"Checking {lock=} and {key=}")
    for i in range(len(lock[0])):
        this_size = [lock[x][i] for x in range(size)].count(FILL) + [key[x][i] for x in range(size)].count(FILL)
        # print(f"\t{this_size=} and should be < {size=}")
        if this_size > size:
            # print(f"Does not fit")
            return False
    # print(f"Fits!")
    return True


@aoc_timed_solution(2024, 25, 1)
def run_part1(filename):
    locks, keys = read(filename)

    print(f"{locks=}")
    print(f"{keys=}")

    fits = 0
    for lock in locks:
        for key in keys:
            fits += does_fit(lock, key)

    return fits


@aoc_timed_solution(2024, 25, 2)
def run_part2(filename):
    pass


if __name__ == '__main__':
    run_part1("example_1.txt")
    run_part1("input.txt")
    # run_part2("example_1.txt")
    # run_part2("input.txt")
