from util.decorators import aoc_timed_solution
from util.reader import read_split_to_2d_array
from util.util import transpose_2d


@aoc_timed_solution(2024, 1, 1)
def run_part1(filename):
    matrix = transpose_2d(read_split_to_2d_array(filename, _type=int, remove_ws=True))
    matrix[0].sort()
    matrix[1].sort()
    return sum([abs(matrix[0][i] - matrix[1][i]) for i in range(len(matrix[0]))])


@aoc_timed_solution(2024, 1, 2)
def run_part2(filename):
    matrix = transpose_2d(read_split_to_2d_array(filename, _type=int, remove_ws=True))
    score = 0
    for i in range(len(matrix[0])):
        score += matrix[0][i] * matrix[1].count(matrix[0][i])
    return score


if __name__ == "__main__":
    run_part1("example_1.txt")  # 11
    run_part1("input.txt")
    run_part2("example_1.txt")  # 31
    run_part2("input.txt")
