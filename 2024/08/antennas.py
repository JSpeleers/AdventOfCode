from itertools import combinations

from util.decorators import aoc_timed_solution


def read_antennas(filename):
    antennas = {}
    rows, cols = 0, 0
    with open(filename) as file:
        for i, line in enumerate(file):
            rows += 1
            cols = len(line)
            for j, char in enumerate(line.strip()):
                if char != '.':
                    if char in antennas:
                        antennas[char].append((i, j))
                    else:
                        antennas[char] = [(i, j)]
    return rows, cols, antennas


def generate_possible_antinodes(coord, diff_x, diff_y, count=1):
    x, y = coord
    antinodes = []
    for i in range(1, count + 1):
        antinodes += [(x + diff_x * i, y + diff_y * i), (x - diff_x * i, y - diff_y * i)]
    return antinodes


def count_antinodes_in_bounds(coords, rows, cols, replicate=False):
    antinodes = []

    for coord1, coord2 in combinations(coords, 2):
        d_x = coord2[0] - coord1[0]
        d_y = coord2[1] - coord1[1]

        if replicate:
            reflections = generate_possible_antinodes(coord1, d_x, d_y, count=rows + cols) + \
                          generate_possible_antinodes(coord2, d_x, d_y, count=rows + cols)
        else:
            reflections = generate_possible_antinodes(coord1, d_x, d_y) + \
                          generate_possible_antinodes(coord2, d_x, d_y)

        antinodes += [(x, y) for x, y in reflections if
                      0 <= x < cols and 0 <= y < rows and (replicate or (x, y) != coord1 and (x, y) != coord2)]

    return antinodes


@aoc_timed_solution(2024, 8, 1)
def run_part1(filename):
    rows, cols, antennas = read_antennas(filename)
    antinodes = []
    for freq in antennas:
        antinodes += count_antinodes_in_bounds(antennas[freq], rows, cols)
    return len(set(antinodes))


@aoc_timed_solution(2024, 8, 2)
def run_part2(filename):
    rows, cols, antennas = read_antennas(filename)
    antinodes = []
    for freq in antennas:
        antinodes += count_antinodes_in_bounds(antennas[freq], rows, cols, replicate=True)
    return len(set(antinodes))


if __name__ == '__main__':
    run_part1("example_1.txt")  # 14
    run_part1("input.txt")
    run_part2("example_1.txt")  # 34
    run_part2("input.txt")
