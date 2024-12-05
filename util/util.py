from functools import reduce
from math import gcd


def lcm(denominators):
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)


MOVE_UP = (-1, 0, 'up')
MOVE_DOWN = (1, 0, 'down')
MOVE_LEFT = (0, -1, 'left')
MOVE_RIGHT = (0, 1, 'right')
MOVES = [MOVE_UP, MOVE_DOWN, MOVE_RIGHT, MOVE_LEFT]

MOVE_UP_LEFT = (-1, -1, 'up-left')
MOVE_UP_RIGHT = (-1, 1, 'up-right')
MOVE_DOWN_LEFT = (1, -1, 'down-left')
MOVE_DOWN_RIGHT = (1, 1, 'down-right')
DIAGONAL_MOVES = [MOVE_UP_LEFT, MOVE_UP_RIGHT, MOVE_DOWN_LEFT, MOVE_DOWN_RIGHT]

ALL_MOVES = [MOVE_UP, MOVE_DOWN, MOVE_RIGHT, MOVE_LEFT, MOVE_UP_LEFT, MOVE_UP_RIGHT, MOVE_DOWN_LEFT, MOVE_DOWN_RIGHT]


def get_neighbors_p(matrix, pos, _type='object', include_diagonals=False):
    return get_neighbors_rc(matrix, pos[0], pos[1], _type=_type, include_diagonals=include_diagonals)


def get_neighbors_rc(matrix, row, col, _type='object', include_diagonals=False):
    neighbors = []
    moves = ALL_MOVES if include_diagonals else MOVES
    for move in moves:
        try:
            new_row = row + move[0]
            if new_row < 0:
                continue
            new_col = col + move[1]
            if new_col < 0:
                continue
            neighbor = matrix[new_row][new_col]
            if _type == 'object':
                neighbors.append(neighbor)
            elif _type == 'coords':
                neighbors.append((new_row, new_col))
            else:
                raise ValueError(f'Invalid _type param "{_type}"')
        except IndexError:
            pass
    return neighbors


def get_in_direction(matrix, row, col, row_diff, col_diff, amount):
    result = []
    for i in range(1, amount + 1):
        new_row = row + row_diff * i
        new_col = col + col_diff * i
        if new_row < 0 or new_col < 0:
            break
        try:
            result.append(matrix[new_row][new_col])
        except IndexError:
            break
    return result


def transpose_2d(arr):
    return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
