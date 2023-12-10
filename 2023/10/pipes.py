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
    pipes.clear()
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
        return f'{self.char}({self.x},{self.y})'

    def get_all_adj_coords(self):
        return [self.get_adj_coords(orientation) for orientation in orientations if self.has_adj(orientation)]

    def get_all_coords(self):
        return [self.get_adj_coords(orientation) for orientation in orientations]

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
    for orientation in orientations:
        path_length = _count_path(start, orientation)
        if path_length is not None and path_length > 0:
            return int((path_length - 1) / 2)
    return None


def _count_path(pipe: Pipe, orientation, length=0):
    if pipe.char == 'S' and length != 0:
        return length + 1
    if pipe.has_adj(orientation):
        # print(f'pipe {pipe} has {orientation}')
        adj_x, adj_y = pipe.get_adj_coords(orientation)
        adj_pipe = _find_pipe(adj_x, adj_y)
        if adj_pipe is not None and adj_pipe.has_adj(reverse_of[orientation]):
            # print(f'{adj_pipe} and next is {adj_pipe.next_orientation(reverse_of[orientation])}')
            return _count_path(adj_pipe, adj_pipe.next_orientation(reverse_of[orientation]), length + 1)
    return None


def _find_pipe(x, y) -> Pipe | None:
    try:
        if x < 0 or y < 0:
            return None
        return pipes[x][y]
    except IndexError:
        return None


@aoc_solution(2023, 10, 2)
def run_part2(filename):
    print()
    start = _read_input(filename)
    path = []
    for orientation in orientations:
        path = _build_path(start, orientation, set())
        if path is not None and len(path) > 0:
            break
    sections = _build_sections(path)
    for section in sections:
        print(f'{len(section)} = {section}')
    return _count_inside_sections(sections, path)


def _build_path(pipe: Pipe, orientation, path):
    if pipe.char == 'S' and len(path) != 0:
        return path
    if pipe.has_adj(orientation):
        # print(f'pipe {pipe} has {orientation}')
        adj_x, adj_y = pipe.get_adj_coords(orientation)
        adj_pipe = _find_pipe(adj_x, adj_y)
        if adj_pipe is not None and adj_pipe.has_adj(reverse_of[orientation]):
            # print(f'{adj_pipe} and next is {adj_pipe.next_orientation(reverse_of[orientation])}')
            path.add(pipe)
            return _build_path(adj_pipe, adj_pipe.next_orientation(reverse_of[orientation]), path)
    return None


def _build_sections(path):  # Flood fill
    section_list = []
    traversed_pipes = set()
    for pipeline in pipes:
        for pipe in pipeline:
            if pipe not in traversed_pipes and pipe not in path:
                found_section = _build_section(pipe, set(), path)
                section_list.append(found_section)
                traversed_pipes = traversed_pipes.union(found_section)
    return section_list


def _build_section(current_pipe: Pipe, traversed_pipes, path):
    # print(f'Building section for {current_pipe}')
    if current_pipe in traversed_pipes or current_pipe in path:
        return traversed_pipes
    else:
        traversed_pipes.add(current_pipe)
        for coord in current_pipe.get_all_coords():
            # print(f'Finding pipe for {coord}')
            new_pipe = _find_pipe(coord[0], coord[1])
            if new_pipe is not None:
                # print(f'From {current_pipe} to {new_pipe}')
                traversed_pipes = traversed_pipes.union(_build_section(new_pipe, traversed_pipes, path))
    return traversed_pipes


def _count_inside_sections(sections, path):
    count = 0
    for section in sections:
        current_pipe = section.pop()
        if current_pipe.x == 0 or current_pipe.y == 0:
            continue
        else:
            lefties = _count_number_of_path_to_the_left(current_pipe, path)
            # print(f'Counting liefties for {current_pipe} = {lefties}')
            if lefties > 0 and lefties % 2 != 0:
                # print(f'Found inside section {section}')
                count += len(section) + 1
    return count


def _count_number_of_path_to_the_left(pipe: Pipe, path):
    count = 0
    y = pipe.y - 1
    while y >= 0:
        count = count + 1 if pipes[pipe.x][y] in path else count
        y -= 1
    return count


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    run_part1("example_1.txt")  # 4
    run_part1("example_2.txt")  # 8
    run_part1("input.txt")
    run_part2("example_3.1.txt")  # 4
    run_part2("example_3.2.txt")  # 4
    run_part2("example_4.txt")  # 8
    # run_part2("example_5.txt")  # 10
    # run_part2("input.txt")
