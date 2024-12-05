from util.decorators import aoc_timed_solution
from util.reader import read_to_array
from util.util import ALL_MOVES, get_in_direction, DIAGONAL_MOVES


@aoc_timed_solution(2024, 4, 1)
def run_part1(filename):
    data = read_to_array(filename)
    counter = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == "X":
                for move in ALL_MOVES:
                    xmas = get_in_direction(data, i, j, move[0], move[1], 3)
                    if 'X' + ''.join(xmas) == 'XMAS':
                        counter += 1
    return counter


@aoc_timed_solution(2024, 4, 2)
def run_part2(filename):
    data = read_to_array(filename)
    counter = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == "A":
                xmas = [get_in_direction(data, i, j, move[0], move[1], 1) for move in DIAGONAL_MOVES]
                xmas = ''.join([item for sublist in xmas for item in sublist])
                if xmas in ['MMSS', 'SMSM', 'SSMM', 'MSMS']:
                    counter += 1
    return counter


if __name__ == "__main__":
    run_part1("example_1.txt")  # 18
    run_part1("input.txt")
    run_part2("example_1.txt")  # 9
    run_part2("input.txt")
