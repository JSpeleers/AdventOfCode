from functools import reduce
from math import gcd


def lcm(denominators):
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)


MOVE_UP = (-1, 0, 'up')
MOVE_DOWN = (1, 0, 'down')
MOVE_LEFT = (0, -1, 'left')
MOVE_RIGHT = (0, 1, 'right')
MOVES = [MOVE_UP, MOVE_DOWN, MOVE_RIGHT, MOVE_LEFT]


def get_neighbors_p(matrix, pos, _type='object'):
    return get_neighbors_rc(matrix, pos[0], pos[1], _type=_type)


def get_neighbors_rc(matrix, row, col, _type='object'):
    neighbors = []
    for move in MOVES:
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


def transpose_2d(arr):
    return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
