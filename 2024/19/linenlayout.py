from functools import cache

from util.decorators import aoc_timed_solution

TOWEL_DICT = {}


def read(filename):
    with open(filename) as file:
        lines = file.readlines()
    return [(i, len(i)) for i in lines[0].strip().split(', ')], [i.strip() for i in lines[2:]]


@cache
def pattern_possible(towel_file, to_find):
    l_to_find = len(to_find)
    for towel, length in TOWEL_DICT[towel_file]:
        if l_to_find > length and towel == to_find[:length]:
            # Divide and conquer
            if pattern_possible(towel_file, to_find[length:]):
                return True
        elif l_to_find == length and towel == to_find:
            return True
    return False


@cache
def count_possible_patterns(towel_file, to_find):
    l_to_find = len(to_find)
    counts = 0
    for towel, length in TOWEL_DICT[towel_file]:
        if l_to_find > length and towel == to_find[:length]:
            # Divide and conquer
            counts += count_possible_patterns(towel_file, to_find[length:])
        elif l_to_find == length and towel == to_find:
            counts += 1
    return counts


@aoc_timed_solution(2024, 19, 1)
def run_part1(filename):
    towels, combinations = read(filename)
    TOWEL_DICT[filename] = towels
    return sum(1 for combo in combinations if pattern_possible(filename, combo))


@aoc_timed_solution(2024, 19, 2)
def run_part2(filename):
    towels, combinations = read(filename)
    TOWEL_DICT[filename] = towels
    return sum(count_possible_patterns(filename, combo) for combo in combinations)


if __name__ == "__main__":
    run_part1("example_1.txt")  # 6
    run_part1("input.txt")
    run_part2("example_1.txt")  # 16
    run_part2("input.txt")
