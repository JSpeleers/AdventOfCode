import numpy as np

from util.decorators import aoc_timed_solution


def _read_input(filename):
    with open(filename) as file:
        text = []
        for i, line in enumerate(file):
            text.append([])
            for c in line.rstrip():
                text[i].append(c)
    return text


@aoc_timed_solution(2023, 11, 1)
def run_part1(filename):
    star_map = _read_input(filename)
    star_map = _do_cosmic_expansion(star_map)
    return _sum_shortest_paths(star_map)


def _sum_shortest_paths(star_map):
    planets = [(x, y) for x, row in enumerate(star_map) for y, c in enumerate(row) if c == '#']
    # print(f'Got {len(planets)} planets')
    path_steps = 0
    for i in range(0, len(planets)):
        for j in range(i + 1, len(planets)):
            path_steps += abs(planets[i][1] - planets[j][1]) + abs(planets[i][0] - planets[j][0])
    return path_steps


@aoc_timed_solution(2023, 11, 2)
def run_part2(filename, multiplier):
    star_map = _read_input(filename)
    rows, columns = _get_cosmic_expansion(np.array(star_map))
    return _sum_shortest_paths_with_expansion(star_map, rows, columns, multiplier=multiplier)


def _sum_shortest_paths_with_expansion(star_map, rows, colums, multiplier=10):
    planets = [(x, y) for x, row in enumerate(star_map) for y, c in enumerate(row) if c == '#']
    # print(f'Got {len(planets)} planets')
    # print(f'And rows {rows} and columns {colums}')
    counter = 0
    path_steps = 0
    for i in range(0, len(planets)):
        for j in range(i + 1, len(planets)):
            path_steps += abs(planets[i][1] - planets[j][1]) + abs(planets[i][0] - planets[j][0])
            crossed_rows = [row for row in rows if
                            planets[i][0] < row < planets[j][0] or planets[j][0] < row < planets[i][0]]
            crossed_columns = [col for col in colums if
                               planets[i][1] < col < planets[j][1] or planets[j][1] < col < planets[i][1]]
            path_steps += (len(crossed_rows) + len(crossed_columns)) * (multiplier - 1)
            counter += 1
    return path_steps


def _do_cosmic_expansion(star_map):
    star_map = np.array(star_map)
    rows, columns = _get_cosmic_expansion(star_map)

    for i, row in enumerate(rows):
        star_map = np.insert(star_map, row + i, '.' * len(star_map), axis=0)
    for i, col in enumerate(columns):
        star_map = np.insert(star_map, col + i, '.' * len(star_map[0]), axis=1)

    return star_map


def _get_cosmic_expansion(star_map):
    return _get_ids_to_expand(star_map), _get_ids_to_expand(star_map.T)


def _get_ids_to_expand(star_map):
    return [i for i in range(len(star_map)) if '#' not in star_map[i]]


if __name__ == "__main__":
    run_part1("example_1.txt")
    run_part1("input.txt")
    run_part2("example_1.txt", 10)  # 1030
    run_part2("example_1.txt", 100)  # 8410
    run_part2("input.txt", 1000000)
