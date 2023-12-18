from util.decorators import aoc_timed_solution

direction_map = ['R', 'D', 'L', 'U']


def _read_input(filename):
    with open(filename) as file:
        instructions = [(line.split()[0], int(line.split()[1])) for line in file]
    return instructions


def _read_second_input(filename):
    def pl(line):
        t = line.split()[2][2:-1]
        return direction_map[int(t[-1])], int(t[:-1], 16)

    with open(filename) as file:
        instructions = [pl(line) for line in file]
    return instructions


@aoc_timed_solution(2023, 18, 1)
def run_part1(filename):
    instructions = _read_input(filename)
    corners, total_edge = _traverse(instructions)
    return _area_shoelace_formula([t[0] for t in corners], [t[1] for t in corners]) + (total_edge // 2 + 1)


def _traverse(instructions):
    row, col = 0, 0
    corners = [(row, col)]
    total_edge = 1
    for (di, val) in instructions:
        if di == 'R':
            col += val
        elif di == 'L':
            col -= val
        elif di == 'U':
            row -= val
        elif di == 'D':
            row += val
        total_edge += val
        corners.append((row, col))
    return corners, total_edge


def _area_shoelace_formula(x, y):
    return int(abs(sum(i * j for i, j in zip(x, y[1:] + y[:1])) - sum(i * j for i, j in zip(x[1:] + x[:1], y))) / 2)


@aoc_timed_solution(2023, 18, 2)
def run_part2(filename):
    instructions = _read_second_input(filename)
    corners, total_edge = _traverse(instructions)
    return _area_shoelace_formula([t[0] for t in corners], [t[1] for t in corners]) + (total_edge // 2 + 1)


if __name__ == "__main__":
    run_part1("example_1.txt")  # 62
    run_part1("input.txt")
    run_part2("example_1.txt")  # 952408144115
    run_part2("input.txt")
