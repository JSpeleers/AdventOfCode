import numpy as np

from util.decorators import aoc_timed_solution


def _read_input(filename):
    text = []
    with open(filename) as file:
        pattern = []
        for i, line in enumerate(file):
            if line.rstrip() == '':
                text.append(np.array(pattern))
                pattern = []
            else:
                pattern.append(list(line.strip()))
        text.append(np.array(pattern))
    return text


def _run(filename, compare_func):
    patterns = _read_input(filename)
    count = 0
    for pattern in patterns:
        count += _reflection(pattern, compare_func)
    return count


@aoc_timed_solution(2023, 13, 1)
def run_part1(filename):
    return _run(filename, np.array_equal)


def _reflection(pattern, compare_func):
    horizontal = _find_reflection_index(pattern, compare_func)  # Horizontal
    if horizontal is None:
        return _find_reflection_index(pattern.T, compare_func)  # Vertical
    return horizontal * 100


def _find_reflection_index(pattern, compare_func):  # Compare is distance == 0 for P1 and distance == 1 for P2
    pattern_length = len(pattern)
    for i in range(1, len(pattern)):
        first = pattern[:i]
        first = np.flip(first, axis=0)
        second = pattern[i:]
        min_length = min(i, pattern_length - i)
        if compare_func(first[:min_length], second[:min_length]):
            return i
    return None


@aoc_timed_solution(2023, 13, 2)
def run_part2(filename):
    return _run(filename, _distance_one)


def _distance_one(a, b):
    return np.sum(abs(np.subtract(_to_numb(a), _to_numb(b))) == 1) == 1


def _to_numb(arr):
    return np.where(arr == '#', 1, np.where(arr == '.', 2, arr)).astype(int)


if __name__ == "__main__":
    run_part1("example_1.txt")  # 405
    run_part1("input.txt")
    run_part2("example_1.txt")  # 400
    run_part2("input.txt")
