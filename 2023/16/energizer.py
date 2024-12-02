import sys

from util.decorators import aoc_timed_solution
from util.reader import read_strip_to_2d_array

# Next X, next Y, coming from
MOVE_UP = (0, -1, 'bottom')
MOVE_DOWN = (0, 1, 'top')
MOVE_LEFT = (-1, 0, 'right')
MOVE_RIGHT = (1, 0, 'left')

char_map = {
    '.': {'top': [MOVE_DOWN], 'bottom': [MOVE_UP], 'left': [MOVE_RIGHT], 'right': [MOVE_LEFT]},
    '/': {'top': [MOVE_LEFT], 'bottom': [MOVE_RIGHT], 'left': [MOVE_UP], 'right': [MOVE_DOWN]},
    '\\': {'top': [MOVE_RIGHT], 'bottom': [MOVE_LEFT], 'left': [MOVE_DOWN], 'right': [MOVE_UP]},
    '-': {'top': [MOVE_LEFT, MOVE_RIGHT], 'bottom': [MOVE_LEFT, MOVE_RIGHT], 'left': [MOVE_RIGHT],
          'right': [MOVE_LEFT]},
    '|': {'top': [MOVE_DOWN], 'bottom': [MOVE_UP], 'left': [MOVE_UP, MOVE_DOWN], 'right': [MOVE_UP, MOVE_DOWN]},
}


@aoc_timed_solution(2023, 16, 1)
def run_part1(filename):
    square = read_strip_to_2d_array(filename)
    return _traverse(square, 0, 0, 'left', set())


def _traverse(square, x, y, coming_from, traversed):
    if (x, y, coming_from) in traversed:
        # Already had this path
        return 0
    if x < 0 or y < 0 or x >= len(square[0]) or y >= len(square):
        # Outside of square
        return 0

    char = square[y][x]
    add = 1 if (x, y) not in [(x, y) for (x, y, _) in traversed] else 0
    traversed.add((x, y, coming_from))
    # print(f'Traversing {char} ({x, y}) coming from the {coming_from}')
    # _print_square(square, (x, y), traversed)
    count = 0
    for (next_x, next_y, cfrom) in char_map[char][coming_from]:
        count += _traverse(square, x + next_x, y + next_y, cfrom, traversed)
    return count + add


def _print_square(square, this, traversed):
    string = ''
    traversed = [(x, y) for (x, y, _) in traversed]
    for y, line in enumerate(square):
        for x, c in enumerate(line):
            string += 'X' if (x, y) == this else '#' if (x, y) in traversed else c
        string += '\n'
    print(string)


@aoc_timed_solution(2023, 16, 2)
def run_part2(filename):
    square = read_strip_to_2d_array(filename)
    all_traverses = [_traverse(square, x, y, cfrom, set()) for (y, x, cfrom) in _get_edges(square)]
    return max(all_traverses)


def _get_edges(square):
    rows, cols = len(square), len(square[0])
    edge_coordinates = []

    for col in range(cols):
        edge_coordinates.append((0, col, 'top'))  # Top
        edge_coordinates.append((rows - 1, col, 'bottom'))  # Bottom

    for row in range(0, rows):
        edge_coordinates.append((row, 0, 'left'))  # Left
        edge_coordinates.append((row, cols - 1, 'right'))  # Right

    return edge_coordinates


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    run_part1("example_1.txt")  # 46
    run_part1("input.txt")
    run_part2("example_1.txt")  # 51
    run_part2("input.txt")
