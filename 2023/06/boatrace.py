from functools import reduce
from operator import mul

from util.decorators import aoc_solution


@aoc_solution(2023, 6, 1)
def run_part1(filename):
    with open(filename) as file:
        races = [[int(num) for num in line.split() if num.isdigit()] for line in file]
    return reduce(mul, [_get_number_of_wins(races[0][i], races[1][i]) for i in range(len(races[0]))])


def _get_number_of_wins(time, max_distance, start=0):
    count = 0
    for i in range(start, time):
        new_distance = i * (time - i)
        if new_distance > max_distance:
            count += 1
        elif count > 0 and new_distance < max_distance:
            return count  # Only downhill from here
    return count


@aoc_solution(2023, 6, 2)
def run_part2(filename):
    with open(filename) as file:
        race = [''.join([num for num in line.split() if num.isdigit()]) for line in file]
    return _get_number_of_wins(int(race[0]), int(race[1]), start=14)


if __name__ == "__main__":
    run_part1("example_1.txt")
    run_part1("input.txt")
    run_part2("example_1.txt")
    run_part2("input.txt")
