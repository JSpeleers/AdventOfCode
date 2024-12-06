from util.decorators import aoc_timed_solution
from util.reader import read_strip_to_2d_array

MOVES = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

ROTATIONS = {
    '^': '>',
    'v': '<',
    '<': '^',
    '>': 'v'
}

OBSTACLES = '#'


def find_robot_start(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] in MOVES:
                return r, c
    return None


def get_next_move_and_robot(matrix, _from, char):
    next_pos = _from[0] + MOVES[char][0], _from[1] + MOVES[char][1]
    try:
        if not matrix[next_pos[0]][next_pos[1]] in OBSTACLES:
            return next_pos, char
        else:
            next_char = ROTATIONS[char]
            next_pos = _from[0] + MOVES[next_char][0], _from[1] + MOVES[next_char][1]
            return next_pos, next_char
    except IndexError:
        return next_pos, None


def traverse_path(matrix, pos):
    history = [[pos, matrix[pos[0]][pos[1]]]]
    lookup_hist = set(str(pos[0]) + "." + str(pos[1]) + matrix[pos[0]][pos[1]])
    next_pos, next_robot = get_next_move_and_robot(matrix, pos, matrix[pos[0]][pos[1]])
    history.append([next_pos, next_robot])
    lookup_hist.add(str(next_pos[0]) + "." + str(next_pos[1]) + next_robot)
    while next_robot:
        next_pos, next_robot = get_next_move_and_robot(matrix, next_pos, next_robot)
        if (next_lookup_hist_str := str(next_pos[0]) + "." + str(next_pos[1]) + str(next_robot)) in lookup_hist:
            return None
        history.append([next_pos, next_robot])
        lookup_hist.add(next_lookup_hist_str)
    return history


@aoc_timed_solution(2024, 6, 1)
def run_part1(filename):
    matrix = read_strip_to_2d_array(filename)
    init = find_robot_start(matrix)
    path = traverse_path(matrix, init)
    return len(set([pos for pos, _ in path[:-1]]))


@aoc_timed_solution(2024, 6, 2)
def run_part2(filename):
    matrix = read_strip_to_2d_array(filename)
    init = find_robot_start(matrix)
    path = traverse_path(matrix, init)
    count = 0
    for pos in set([pos for pos, _ in path[:-1]]):
        if pos != init:
            matrix[pos[0]][pos[1]] = OBSTACLES
            new_path = traverse_path(matrix, init)
            if not new_path:
                count += 1
            matrix[pos[0]][pos[1]] = '.'
    return count


if __name__ == '__main__':
    run_part1("example_1.txt")  # 41
    run_part1("input.txt")
    run_part2("example_1.txt")  # 6
    run_part2("input.txt")  # 1796
