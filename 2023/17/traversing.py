import sys

from util.decorators import aoc_timed_solution
from util.reader import read_strip_to_2d_array

# Next row, next col, moved to
MOVE_UP = (-1, 0, 'up')
MOVE_DOWN = (1, 0, 'down')
MOVE_LEFT = (0, -1, 'left')
MOVE_RIGHT = (0, 1, 'right')


@aoc_timed_solution(2023, 17, 1)
def run_part1(filename):
    matrix = read_strip_to_2d_array(filename, int)
    start = (0, 0)
    end = (len(matrix) - 1, len(matrix[0]) - 1)
    return dfs_with_constraints(matrix, start, end, set(), 0, sys.maxsize, [])


def dfs_with_constraints(matrix, current_node, end_node, traversed, current_weight, best_weight, last_moves, times=3):
    if current_node in traversed:
        return sys.maxsize
    traversed.add(current_node)
    row, col = current_node
    current_weight += matrix[row][col]
    if current_node == end_node:
        print(f'End reached with weight {current_weight}')
        return current_weight
    if current_weight > best_weight:
        print(f'Suboptimal path, pruning {current_weight}')
        return current_weight

    moves = _get_moves(matrix, row, col, last_moves, times)
    print(f'At {current_node} and got moves {moves}')
    weights = []
    for move in moves:
        add_row, add_col, direction = move
        last_moves.append(direction)
        if len(last_moves) > times:
            last_moves.pop(0)
        next_node = (row + add_row, col + add_col)
        weight = dfs_with_constraints(matrix, next_node, end_node, traversed, current_weight, best_weight, last_moves,
                                      times)
        weights.append(weight)
    return min(weights)


def _get_moves(matrix, row, col, last_moves, times):
    moves = []
    if row > 0 and last_moves.count('up') < times and (len(last_moves) == 0 or last_moves[-1] != 'down'):
        moves.append(MOVE_UP)
    if col > 0 and last_moves.count('left') < times and (len(last_moves) == 0 or last_moves[-1] != 'right'):
        moves.append(MOVE_LEFT)
    if row < len(matrix) - 1 and last_moves.count('down') < times and (len(last_moves) == 0 or last_moves[-1] != 'up'):
        moves.append(MOVE_DOWN)
    if col < len(matrix[0]) - 1 and last_moves.count('right') < times and (
            len(last_moves) == 0 or last_moves[-1] != 'left'):
        moves.append(MOVE_RIGHT)

    return moves


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    run_part1("example_1.txt")  # 46
    # run_part1("input.txt")
    # run_part2("example_1.txt")  # 51
    # run_part2("input.txt")
