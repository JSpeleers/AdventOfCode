import math
import sys
from collections import defaultdict

from util.decorators import aoc_timed_solution
from util.util import get_neighbors_p

sys.setrecursionlimit(10 ** 6)

WALL = "#"
SPACE = "."


def read(filename):
    with open(filename) as file:
        return [tuple(map(int, line.strip().split(","))) for line in file]


def pretty_print_2d(matrix):
    for row in matrix:
        print("".join(row))


def calculate_distances(matrix, node, dist_dict):
    neighbors = [
        n
        for n in get_neighbors_p(matrix, node, _type="coords")
        if matrix[n[0]][n[1]] != WALL and dist_dict[node] + 1 < dist_dict[n]
    ]
    for n in neighbors:
        dist_dict[n] = dist_dict[node] + 1
    for n in neighbors:
        calculate_distances(matrix, n, dist_dict)


@aoc_timed_solution(2024, 18, 1)
def run_part1(filename, size, byte_count):
    bytes = read(filename)[:byte_count]
    start = (0, 0)
    end = (size - 1, size - 1)
    matrix = [[SPACE for _ in range(size)] for _ in range(size)]
    for b in bytes:
        matrix[b[1]][b[0]] = WALL

    dist_dict = defaultdict(lambda: math.inf, {start: 0})
    # print(dist_dict)
    calculate_distances(matrix, start, dist_dict)
    # print(dist_dict)
    return dist_dict[end]


@aoc_timed_solution(2024, 18, 2)
def run_part2(filename, size, byte_count):
    start = (0, 0)
    end = (size - 1, size - 1)
    dist_dict = defaultdict(lambda: math.inf, {start: 0})
    bytes = []
    while dist_dict[end] != math.inf or len(bytes) == 0:
        bytes = read(filename)[:byte_count]
        matrix = [[SPACE for _ in range(size)] for _ in range(size)]
        for b in bytes:
            matrix[b[1]][b[0]] = WALL

        dist_dict = defaultdict(lambda: math.inf, {start: 0})
        calculate_distances(matrix, start, dist_dict)
        byte_count += 1
    return bytes.pop()


if __name__ == "__main__":
    run_part1("example_1.txt", 7, 12)  # 22
    run_part1("input.txt", 71, 1024)
    run_part2("input.txt", 71, 2500)
