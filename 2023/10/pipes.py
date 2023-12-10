import sys

from util.decorators import aoc_solution

orientations = ['top', 'bottom', 'left', 'right']

reverse_of = {'top': 'bottom', 'bottom': 'top', 'left': 'right', 'right': 'left'}

orientation_map = {
    '|': {'top': True, 'bottom': True, 'left': False, 'right': False},
    '-': {'top': False, 'bottom': False, 'left': True, 'right': True},
    'L': {'top': True, 'bottom': False, 'left': False, 'right': True},
    'J': {'top': True, 'bottom': False, 'left': True, 'right': False},
    '7': {'top': False, 'bottom': True, 'left': True, 'right': False},
    'F': {'top': False, 'bottom': True, 'left': False, 'right': True},
    '.': {'top': False, 'bottom': False, 'left': False, 'right': False},
    'S': {'top': True, 'bottom': True, 'left': True, 'right': True}
}

pipes = []


def _read_input(filename):
    with open(filename) as file:
        for i, line in enumerate(file):
            line = line.rstrip()
            pipes.append([])
            for j, c in enumerate(line):
                pipes[i].append(Pipe(c, i, j))
                if c == 'S':
                    start = pipes[i][j]
    return start


class Pipe:

    def __init__(self, char, x, y):
        self.char = char
        self.x = x
        self.y = y

    def __repr__(self):
        return self.char

    def get_all_adj_coords(self):
        return [self.get_adj_coords(orientation) for orientation in orientations if self.has_adj(orientation)]

    def get_adj_coords(self, orientation):
        if orientation == 'top':
            return self.x - 1, self.y
        elif orientation == 'bottom':
            return self.x + 1, self.y
        elif orientation == 'left':
            return self.x, self.y - 1
        elif orientation == 'right':
            return self.x, self.y + 1

    def has_adj(self, orientation):
        return orientation_map[self.char][orientation]

    def next_orientation(self, orientation):
        return \
            [key for key in orientation_map[self.char].keys() if
             orientation_map[self.char][key] and key != orientation][0]


@aoc_solution(2023, 10, 1)
def run_part1(filename):
    start = _read_input(filename)
    paths = [_find_path(start, orientation) for orientation in orientations]
    return paths, int((max([x for x in paths if x is not None]) - 1) / 2)


@aoc_solution(2023, 10, 1)
def run_part1_v2(filename):
    start = _read_input(filename)
    for orientation in orientations:
        path_length = _find_path(start, orientation)
        if path_length is not None and path_length > 0:
            return int((path_length - 1) / 2)

    return


def _find_path(pipe: Pipe, orientation, length=0):
    if pipe.char == 'S' and length != 0:
        return length + 1
    if pipe.has_adj(orientation):
        # print(f'pipe {pipe} has {orientation}')
        adj_x, adj_y = pipe.get_adj_coords(orientation)
        adj_pipe = _find_pipe(adj_x, adj_y)
        if adj_pipe is not None and adj_pipe.has_adj(reverse_of[orientation]):
            # print(f'{adj_pipe} and next is {adj_pipe.next_orientation(reverse_of[orientation])}')
            return _find_path(adj_pipe, adj_pipe.next_orientation(reverse_of[orientation]), length + 1)
    return None


def _find_pipe(x, y) -> Pipe | None:
    try:
        return pipes[x][y]
    except IndexError:
        return None


if __name__ == "__main__":
    sys.setrecursionlimit(1000000000)
    run_part1("example_1.txt")  # 4
    run_part1("example_2.txt")  # 8
    run_part1_v2("example_1.txt")  # 4
    run_part1_v2("example_2.txt")  # 8
    run_part1_v2("input.txt")
