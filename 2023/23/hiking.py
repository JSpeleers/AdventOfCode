import sys

from util.decorators import aoc_solution
from util.reader import read_to_2d_array
from util.util import get_neighbors_p, MOVE_RIGHT, MOVE_LEFT, MOVE_DOWN, MOVE_UP

SLIDES = {'>': MOVE_RIGHT, '<': MOVE_LEFT, 'v': MOVE_DOWN, '^': MOVE_UP}


@aoc_solution(2023, 23, 1)
def run_part1(filename):
    matrix = read_to_2d_array(filename)
    start = (0, matrix[0].index('.'))
    matrix[-1][matrix[-1].index('.')] = 'E'
    return _traverse(matrix, start, 0, set())


def _traverse(matrix, current, length, traversed):
    char = matrix[current[0]][current[1]]
    if char == 'E':
        return length
    traversed.add(current)
    if char in SLIDES:
        next_moves = [(current[0] + SLIDES[char][0], current[1] + SLIDES[char][1])]
    else:
        next_moves = [i for i in get_neighbors_p(matrix, current, _type='coords') if
                      matrix[i[0]][i[1]] != '#' and i not in traversed]
    print(current, next_moves)
    if len(next_moves) > 0:
        return max([_traverse(matrix, move, length + 1, traversed) for move in next_moves])
    return -1


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    run_part1("example_1.txt")  # 94
    run_part1("input.txt")
