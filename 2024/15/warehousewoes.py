from copy import deepcopy

from util.decorators import aoc_timed_solution
from util.util import SLIDES, pretty_print_2d

ROBOT = '@'
WALL = '#'
OBJ = 'O'
SPACE = '.'


def read(filename):
    with open(filename) as file:
        str_matrix, str_moves = file.read().split('\n\n')
    return [list(x) for x in str_matrix.split('\n')], list(str_moves)


def find_start(matrix, char='@'):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == char:
                return (i, j)
    return None


def is_viable_move(matrix, pos, move):
    pos_r, pos_c = pos
    if SLIDES[move][2] == 'right':
        sub = matrix[pos_r][pos_c:]
    elif SLIDES[move][2] == 'left':
        sub = matrix[pos_r][:pos_c]
    elif SLIDES[move][2] == 'up':
        sub = [matrix[i][pos_c] for i in range(0, pos_r)]
    else:  # down
        sub = [matrix[i][pos_c] for i in range(pos_r, len(matrix[pos_r]))]
    print(f"{sub=} because {SLIDES[move][2]=}")
    return SPACE in sub


def do_move(matrix, pos, move, pushed_char):
    pos_r, pos_c = pos
    m_r, m_c, _ = SLIDES[move]
    new_pos_r, new_pos_c = pos_r + m_r, pos_c + m_c
    if matrix[new_pos_r][new_pos_c] == SPACE:
        matrix[new_pos_r][new_pos_c] = pushed_char
        return
    elif matrix[new_pos_r][new_pos_c] == OBJ:
        matrix[new_pos_r][new_pos_c] = pushed_char
        return do_move(matrix, (new_pos_r, new_pos_c), move, OBJ)
    else:
        raise ValueError("not expecting anything different than a space or object to push")


@aoc_timed_solution(2024, 15, 1)
def run_part1(filename):
    matrix, moves = read(filename)
    pos = find_start(matrix)
    for move in [m for m in moves if m != '\n']:
        # print(f"Move: {move}")
        og_matrix = deepcopy(matrix)
        try:
            do_move(matrix, pos, move, ROBOT)
            matrix[pos[0]][pos[1]] = SPACE
            pos = pos[0] + SLIDES[move][0], pos[1] + SLIDES[move][1]
        except ValueError:
            matrix = og_matrix
    pretty_print_2d(matrix)
    boxes = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == OBJ]
    return sum(100 * i + j for i, j in boxes)


@aoc_timed_solution(2024, 15, 2)
def run_part2(filename):
    # TODO
    pass


if __name__ == '__main__':
    run_part1("example_1.txt")  # 2028
    run_part1("example_2.txt")  # 10092
    run_part1("input.txt")
