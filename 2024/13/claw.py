import re

from util.decorators import aoc_timed_solution

pattern = r"X[+=](\d+), Y[+=](\d+)"


def read(filename):
    with open(filename) as file:
        input_string = file.read()
    return [[(int(x), int(y)) for x, y in re.findall(pattern, block)] for block in input_string.split("\n\n")]


@aoc_timed_solution(2024, 13, 1)
def run_part1(filename, add=0):
    equations = read(filename)
    sol = 0
    for equation in equations:
        a_x, a_y = equation[0]
        b_x, b_y = equation[1]
        p_x, p_y = equation[2]
        p_x += add
        p_y += add
        # Cramer's
        A = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
        B = (a_x * p_y - a_y * p_x) / (a_x * b_y - a_y * b_x)
        if A.is_integer() and B.is_integer():
            sol += int(A) * 3 + int(B)
    return sol


@aoc_timed_solution(2024, 13, 2)
def run_part2(filename):
    return run_part1(filename, add=10000000000000)


if __name__ == '__main__':
    run_part1("example_1.txt")  # 480
    run_part1("input.txt")
    # run_part2("example_1.txt")
    run_part2("input.txt")
