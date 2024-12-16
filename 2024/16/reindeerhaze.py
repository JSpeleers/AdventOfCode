import math
import sys
from collections import defaultdict

from util.decorators import aoc_timed_solution
from util.reader import read_strip_to_2d_array
from util.util import get_neighbors_p

START = 'S'
END = 'E'
WALL = '#'
SPACE = '.'

sys.setrecursionlimit(10 ** 6)


def find(matrix, char):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == char:
                return i, j
    return None


def calc_weight(moves):
    s = 0
    current = 'right'
    for m in range(0, len(moves)):
        s += 1 if moves[m][1][2] == current else 1001
        current = moves[m][1][2]
    return s


def traverse(matrix, node, dist_dict, moves_dict, end=None):
    neighbours = [((x, y), z) for (x, y), z in get_neighbors_p(matrix, node, _type='coordsmove') if
                  matrix[x][y] != WALL and dist_dict[(x, y)] > calc_weight(moves_dict[node] + [((x, y), z)])]
    if node == end:
        sols.append(moves_dict[node])
    for n in neighbours:
        moves_dict[n[0]] = moves_dict[node] + [n]
        dist_dict[n[0]] = calc_weight(moves_dict[n[0]])
    for n in neighbours:
        traverse(matrix, n[0], dist_dict, moves_dict)


@aoc_timed_solution(2024, 16, 1)
def run_part1(filename):
    matrix = read_strip_to_2d_array(filename)
    start, end = find(matrix, START), find(matrix, END)
    dist_dict = defaultdict(lambda: math.inf, {start: 0})
    moves_dict = defaultdict(list, {start: []})
    neighbours = [((x, y), z) for (x, y), z in get_neighbors_p(matrix, start, _type='coordsmove') if
                  matrix[x][y] != WALL]
    for n in neighbours:
        moves_dict[n[0]] = [n]
        dist_dict[n[0]] = calc_weight(moves_dict[n[0]])
    for n in neighbours:
        traverse(matrix, n[0], dist_dict, moves_dict)
    return dist_dict[end]


@aoc_timed_solution(2024, 16, 2)
def run_part2(filename):
    matrix = read_strip_to_2d_array(filename)
    start, end = find(matrix, START), find(matrix, END)
    dist_dict = defaultdict(lambda: math.inf, {start: 0})
    moves_dict = defaultdict(list, {start: []})
    neighbours = [((x, y), z) for (x, y), z in get_neighbors_p(matrix, start, _type='coordsmove') if
                  matrix[x][y] != WALL]
    for n in neighbours:
        moves_dict[n[0]] = [n]
        dist_dict[n[0]] = calc_weight(moves_dict[n[0]])
    for n in neighbours:
        traverse(matrix, n[0], dist_dict, moves_dict, end=end)
    # TODO
    return dist_dict[end]


if __name__ == '__main__':
    run_part1("example_1.txt")  # 7036
    run_part1("example_2.txt")  # 11048
    # run_part1("input.txt")

    sols = []
    run_part2("input.txt")
