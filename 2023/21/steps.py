from functools import cache

import numpy as np

from util.decorators import aoc_timed_solution
from util.reader import read_to_2d_array
from util.util import MOVES, get_neighbors_p, MOVE_UP, MOVE_DOWN, MOVE_RIGHT, MOVE_LEFT


@aoc_timed_solution(2023, 21, 1)
def run_part1(filename, steps):
    matrix = np.array(read_to_2d_array(filename))
    s = np.where(matrix == 'S')
    s_pos = s[0][0], s[1][0]
    return _traverse(matrix, s_pos, steps, _moves_from)


def _traverse(matrix, pos, steps, move_fn):
    previous = [pos]
    step = 0
    while step < steps:
        this = move_fn(matrix, previous)
        # print(f'Step {step}\n\t{previous}\n\t{this}\n')
        previous = this
        step += 1
    return len(previous)


def _moves_from(matrix, poss):
    possibilities = set([n for pos in poss for n in get_neighbors_p(matrix, pos, _type='coords')])
    return [r for r in possibilities if matrix[r[0]][r[1]] != '#']


@aoc_timed_solution(2023, 21, 2)
def run_part2(filename, steps):
    matrix = np.array(read_to_2d_array(filename))
    s = np.where(matrix == 'S')
    s_pos = (s[0][0], s[1][0], (0, 0))
    return _traverse(matrix, s_pos, steps, _extended_moves_from)


def _extended_moves_from(matrix, poss):
    possibilities = set([n for pos in poss for n in get_neighbors_extended(pos, len(matrix), len(matrix[0]))])
    return [p for p in possibilities if matrix[p[0]][p[1]] != '#']


@cache
def get_neighbors_extended(pos, rows, cols):
    row, col, ext = pos
    neighbors = []
    for move in MOVES:
        new_row = row + move[0]
        add_ext = (0, 0)
        if new_row < 0:
            new_row = rows - 1
            # print(f'Outside grid: row < 0 thus new row = {new_row}')
            add_ext = MOVE_UP
        elif new_row >= rows:
            new_row = 0
            # print(f'Outside grid: row > len thus new row = {new_row}')
            add_ext = MOVE_DOWN

        new_col = col + move[1]
        if new_col < 0:
            new_col = cols - 1
            # print(f'Outside grid: col < 0 thus new col = {new_col}')
            add_ext = MOVE_LEFT
        elif new_col >= cols:
            new_col = 0
            # print(f'Outside grid: col > len thus new col = {new_col}')
            add_ext = MOVE_RIGHT
        neighbors.append((new_row, new_col, _ext(ext, add_ext)))
    # print(f'{pos} = {neighbors}')
    return neighbors


REVERSE_EXT_MAP = {'u': 'd', 'd': 'u', 'r': 'l', 'l': 'r'}


def _ext(o_ext, n_ext):  # TODO find loops and shorten ext
    # o_ext = (Y extensions, X extensions)
    return o_ext[0] + n_ext[0], o_ext[1] + n_ext[1]


if __name__ == "__main__":
    # run_part1("example_1.txt", 6)  # 16
    # run_part1("input.txt", 64)
    # run_part2("example_1.txt", 6)  # 16
    run_part2("example_1.txt", 10)  # 50
    run_part2("example_1.txt", 50)  # 1594
    run_part2("example_1.txt", 100)  # 6536
    run_part2("example_1.txt", 500)  # 167004
    run_part2("example_1.txt", 1000)  # 668697
    run_part2("example_1.txt", 5000)  # 16733044
    run_part2("input.txt", 26501365)
