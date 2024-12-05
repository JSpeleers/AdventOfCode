import re

from util.decorators import aoc_timed_solution
from util.reader import read_to_array


@aoc_timed_solution(2024, 3, 1)
def run_part1(filename):
    data = read_to_array(filename)
    result = 0
    for line in data:
        matches = re.findall(r"mul\((\d+),(\d+)\)", line)
        result += sum(int(x) * int(y) for x, y in matches)
    return result


@aoc_timed_solution(2024, 3, 2)
def run_part2(filename):
    data = read_to_array(filename)
    result = 0
    should_count = True
    for line in data:
        matches = re.findall(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", line)
        for match in matches:
            if match[0] == "do()":
                should_count = True
            elif match[0] == "don't()":
                should_count = False
            elif should_count:
                result += int(match[1]) * int(match[2])
    return result


if __name__ == '__main__':
    run_part1("example_1.txt")  # 161
    run_part1("input.txt")
    run_part2("example_2.txt")  # 48
    run_part2("input.txt")
