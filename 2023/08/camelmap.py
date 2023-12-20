from util.decorators import aoc_solution, aoc_timed_solution
from util.util import lcm

instr_map = {'L': 0, 'R': 1}


def _read_input(filename):
    instructions = ''
    camelmap = {}
    with open(filename) as file:
        for i, line in enumerate(file):
            if i == 0:
                instructions = line.rstrip()
            elif i > 1:
                camelmap[line.split()[0]] = (line.split()[2][1:-1], line.split()[3][:-1])
    return instructions, camelmap


def _traverse_camelmap(camelmap, instructions, end_cond_func, start_node='AAA'):
    current_node = start_node
    instr_i = 0
    counter = 0
    while not end_cond_func(current_node):
        current_node = camelmap[current_node][instr_map.get(instructions[instr_i])]
        instr_i = (instr_i + 1) % len(instructions)
        counter += 1
    return counter


@aoc_solution(2023, 8, 1)
def run_part1(filename):
    instructions, camelmap = _read_input(filename)
    return _traverse_camelmap(camelmap, instructions, _end_condition_p1)


def _end_condition_p1(node):
    return node == 'ZZZ'


@aoc_timed_solution(2023, 8, 2)
def run_part2(filename):
    instructions, camelmap = _read_input(filename)
    return _traverse_multiplenodes_camelmap_lcm(camelmap, instructions)


def _traverse_multiplenodes_camelmap_lcm(camelmap, instructions):
    return lcm([_traverse_camelmap(camelmap, instructions, _end_condition_p2, start_node=start_node) for start_node in
                [node for node in camelmap.keys() if node[-1] == 'A']])


def _end_condition_p2(node):
    return node[-1] == 'Z'


if __name__ == "__main__":
    run_part1("example_1.txt")
    run_part1("example_2.txt")
    run_part1("input.txt")
    run_part2("example_3.txt")
    run_part2("input.txt")
