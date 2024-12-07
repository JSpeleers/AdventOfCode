from util.decorators import aoc_timed_solution
from util.reader import read_to_array


def mul(a, b): return a * b
def sumz(a, b): return a + b
def concat(a, b): return int(str(a) + str(b))


def find_operators_for_result(goal, current, numbers, count, operations):
    for op in operations:
        new_current = op(current, numbers[0])
        if len(numbers) == 1:
            if new_current == goal:
                count += 1
        else:
            count += find_operators_for_result(goal, new_current, numbers[1:], count, operations)
    return count


def run_with_ops(filename, operations):
    equations = read_to_array(filename)
    counts = 0
    for equation in equations:
        # print(f"{equation}")
        goal, numbers = equation.split(":")
        numbers = [int(x) for x in numbers.split(' ') if x != '']
        count = find_operators_for_result(int(goal), numbers[0], numbers[1:], 0, operations)
        if count > 0:
            counts += int(goal)
            # print(f"Got hit on {equation=} thus {counts=}")
    return counts


@aoc_timed_solution(2024, 7, 1)
def run_part1(filename):
    return run_with_ops(filename, [mul, sumz])


@aoc_timed_solution(2024, 7, 2)
def run_part2(filename):
    return run_with_ops(filename, [mul, sumz, concat])


if __name__ == '__main__':
    run_part1("example_1.txt")  # 3749
    run_part1("input.txt")
    run_part2("example_1.txt")  # 11387
    run_part2("input.txt")
