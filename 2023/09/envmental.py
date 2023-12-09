from numpy.polynomial.polynomial import Polynomial

from util.decorators import aoc_solution, aoc_timed_solution


@aoc_solution(2023, 9, 1)
def run_part1(filename):
    with open(filename) as file:
        result = 0
        for line in file:
            y = [int(x) for x in line.split()]
            polynomial = Polynomial.fit(range(len(y)), y, deg=len(y) - 1)
            result += polynomial(len(y))
    return round(result)


@aoc_timed_solution(2023, 9, 2)
def run_part2(filename):
    with open(filename) as file:
        result = 0
        for line in file:
            y = [int(x) for x in line.split()]
            polynomial = Polynomial.fit(range(len(y)), y, deg=len(y) - 1)
            result += polynomial(-1)
    return round(result)


if __name__ == "__main__":
    run_part1("example_1.txt")
    run_part1("input.txt")
    run_part2("example_1.txt")
    run_part2("input.txt")
