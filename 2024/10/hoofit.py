from util.decorators import aoc_timed_solution
from util.reader import read_strip_to_2d_array
from util.util import get_neighbors_rc


def find_peaks(tmap, r, c, val):
    valid_neighbours = [(x, y) for (x, y) in get_neighbors_rc(tmap, r, c, _type='coords') if tmap[x][y] == val]
    if val == 9:
        return set(str(vnr) + "," + str(vnc) for vnr, vnc in valid_neighbours if tmap[vnr][vnc] == val)
    return {peak for vnr, vnc in valid_neighbours for peak in find_peaks(tmap, vnr, vnc, val + 1)}


def find_hikes(tmap, r, c, val):
    valid_neighbours = [(x, y) for (x, y) in get_neighbors_rc(tmap, r, c, _type='coords') if tmap[x][y] == val]
    if val == 9:
        return sum([1 for vnr, vnc in valid_neighbours if tmap[vnr][vnc] == val])
    return sum(find_hikes(tmap, vnr, vnc, val + 1) for vnr, vnc in valid_neighbours)


def run(filename, method):
    tmap = read_strip_to_2d_array(filename, int)
    return sum(method(tmap, r, c, 1) for r in range(len(tmap)) for c in range(len(tmap)) if tmap[r][c] == 0)


@aoc_timed_solution(2024, 10, 1)
def run_part1(filename):
    return run(filename, lambda tmap, r, c, val: len(find_peaks(tmap, r, c, val)))


@aoc_timed_solution(2024, 10, 2)
def run_part2(filename):
    return run(filename, find_hikes)


if __name__ == '__main__':
    run_part1("example_1.txt")  # 36
    run_part1("input.txt")
    run_part2("example_1.txt")  # 81
    run_part2("input.txt")
