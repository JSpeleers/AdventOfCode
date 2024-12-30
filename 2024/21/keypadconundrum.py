from util.decorators import aoc_timed_solution
from util.reader import read_to_array

import itertools

NUM_PAD = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]
NUM_PAD_MOVES = {('7', '7'): ['A'], ('7', '8'): ['>A'], ('7', '9'): ['>>A'], ('7', '4'): ['vA'],
                 ('7', '5'): ['v>A', '>vA'], ('7', '6'): ['>v>A', 'v>>A', '>>vA'], ('7', '1'): ['vvA'],
                 ('7', '2'): ['v>vA', 'vv>A', '>vvA'],
                 ('7', '3'): ['v>v>A', 'vv>>A', '>v>vA', '>vv>A', 'v>>vA', '>>vvA'],
                 ('7', '0'): ['>vvvA', 'v>vvA', 'vvv>A', 'vv>vA'],
                 ('7', 'A'): ['>vv>vA', 'v>vv>A', 'v>v>vA', 'vv>>vA', '>>vvvA', 'vv>v>A', 'v>>vvA', '>v>vvA', 'vvv>>A',
                              '>vvv>A'], ('8', '7'): ['<A'], ('8', '8'): ['A'], ('8', '9'): ['>A'],
                 ('8', '4'): ['<vA', 'v<A'], ('8', '5'): ['vA'], ('8', '6'): ['v>A', '>vA'],
                 ('8', '1'): ['<vvA', 'vv<A', 'v<vA'], ('8', '2'): ['vvA'], ('8', '3'): ['v>vA', 'vv>A', '>vvA'],
                 ('8', '0'): ['vvvA'], ('8', 'A'): ['>vvvA', 'v>vvA', 'vvv>A', 'vv>vA'], ('9', '7'): ['<<A'],
                 ('9', '8'): ['<A'], ('9', '9'): ['A'], ('9', '4'): ['<<vA', '<v<A', 'v<<A'],
                 ('9', '5'): ['<vA', 'v<A'], ('9', '6'): ['vA'],
                 ('9', '1'): ['<<vvA', '<vv<A', '<v<vA', 'v<<vA', 'vv<<A', 'v<v<A'],
                 ('9', '2'): ['<vvA', 'vv<A', 'v<vA'], ('9', '3'): ['vvA'],
                 ('9', '0'): ['v<vvA', 'vv<vA', 'vvv<A', '<vvvA'], ('9', 'A'): ['vvvA'], ('4', '7'): ['^A'],
                 ('4', '8'): ['^>A', '>^A'], ('4', '9'): ['^>>A', '>>^A', '>^>A'], ('4', '4'): ['A'],
                 ('4', '5'): ['>A'], ('4', '6'): ['>>A'], ('4', '1'): ['vA'], ('4', '2'): ['v>A', '>vA'],
                 ('4', '3'): ['>v>A', 'v>>A', '>>vA'], ('4', '0'): ['v>vA', 'vv>A', '>vvA'],
                 ('4', 'A'): ['v>v>A', 'vv>>A', '>v>vA', '>vv>A', 'v>>vA', '>>vvA'], ('5', '7'): ['^<A', '<^A'],
                 ('5', '8'): ['^A'], ('5', '9'): ['^>A', '>^A'], ('5', '4'): ['<A'], ('5', '5'): ['A'],
                 ('5', '6'): ['>A'], ('5', '1'): ['<vA', 'v<A'], ('5', '2'): ['vA'], ('5', '3'): ['v>A', '>vA'],
                 ('5', '0'): ['vvA'], ('5', 'A'): ['v>vA', 'vv>A', '>vvA'], ('6', '7'): ['^<<A', '<^<A', '<<^A'],
                 ('6', '8'): ['^<A', '<^A'], ('6', '9'): ['^A'], ('6', '4'): ['<<A'], ('6', '5'): ['<A'],
                 ('6', '6'): ['A'], ('6', '1'): ['<<vA', '<v<A', 'v<<A'], ('6', '2'): ['<vA', 'v<A'],
                 ('6', '3'): ['vA'], ('6', '0'): ['<vvA', 'vv<A', 'v<vA'], ('6', 'A'): ['vvA'], ('1', '7'): ['^^A'],
                 ('1', '8'): ['^^>A', '>^^A', '^>^A'],
                 ('1', '9'): ['^^>>A', '>^>^A', '>>^^A', '>^^>A', '^>>^A', '^>^>A'], ('1', '4'): ['^A'],
                 ('1', '5'): ['^>A', '>^A'], ('1', '6'): ['^>>A', '>>^A', '>^>A'], ('1', '1'): ['A'],
                 ('1', '2'): ['>A'], ('1', '3'): ['>>A'], ('1', '0'): ['v>A', '>vA'],
                 ('1', 'A'): ['>v>A', 'v>>A', '>>vA'], ('2', '7'): ['^^<A', '^<^A', '<^^A'], ('2', '8'): ['^^A'],
                 ('2', '9'): ['^^>A', '>^^A', '^>^A'], ('2', '4'): ['^<A', '<^A'], ('2', '5'): ['^A'],
                 ('2', '6'): ['^>A', '>^A'], ('2', '1'): ['<A'], ('2', '2'): ['A'], ('2', '3'): ['>A'],
                 ('2', '0'): ['vA'], ('2', 'A'): ['v>A', '>vA'],
                 ('3', '7'): ['<<^^A', '^<<^A', '^^<<A', '<^^<A', '^<^<A', '<^<^A'],
                 ('3', '8'): ['^^<A', '^<^A', '<^^A'], ('3', '9'): ['^^A'], ('3', '4'): ['^<<A', '<^<A', '<<^A'],
                 ('3', '5'): ['^<A', '<^A'], ('3', '6'): ['^A'], ('3', '1'): ['<<A'], ('3', '2'): ['<A'],
                 ('3', '3'): ['A'], ('3', '0'): ['<vA', 'v<A'], ('3', 'A'): ['vA'],
                 ('0', '7'): ['<^^^A', '^^<^A', '^^^<A', '^<^^A'], ('0', '8'): ['^^^A'],
                 ('0', '9'): ['^^>^A', '^>^^A', '>^^^A', '^^^>A'], ('0', '4'): ['^^<A', '^<^A', '<^^A'],
                 ('0', '5'): ['^^A'], ('0', '6'): ['^^>A', '>^^A', '^>^A'], ('0', '1'): ['^<A', '<^A'],
                 ('0', '2'): ['^A'], ('0', '3'): ['^>A', '>^A'], ('0', '0'): ['A'], ('0', 'A'): ['>A'],
                 ('A', '7'): ['^<^<^A', '<^<^^A', '<^^^<A', '^^<^<A', '^^<<^A', '^<<^^A', '^<^^<A', '^^^<<A', '<^^<^A',
                              '<<^^^A'], ('A', '8'): ['<^^^A', '^^<^A', '^^^<A', '^<^^A'], ('A', '9'): ['^^^A'],
                 ('A', '4'): ['<<^^A', '^<<^A', '^^<<A', '<^^<A', '^<^<A', '<^<^A'],
                 ('A', '5'): ['^^<A', '^<^A', '<^^A'], ('A', '6'): ['^^A'], ('A', '1'): ['^<<A', '<^<A', '<<^A'],
                 ('A', '2'): ['^<A', '<^A'], ('A', '3'): ['^A'], ('A', '0'): ['<A'], ('A', 'A'): ['A']}
DIR_PAD = [[None, '^', 'A'], ['<', 'v', '>']]
DIR_PAD_MOVES = {('^', '^'): ['A'], ('^', 'A'): ['>A'], ('^', '<'): ['<vA', 'v<A'], ('^', 'v'): ['vA'],
                 ('^', '>'): ['v>A', '>vA'], ('A', '^'): ['<A'], ('A', 'A'): ['A'],
                 ('A', '<'): ['<v<A', 'v<<A', '<<vA'], ('A', 'v'): ['<vA', 'v<A'],
                 ('A', '>'): ['vA'], ('<', '^'): ['>^A', '^>A'], ('<', 'A'): ['>^>A', '^>>A', '>>^A'],
                 ('<', '<'): ['A'], ('<', 'v'): ['>A'], ('<', '>'): ['>>A'], ('v', '^'): ['^A'],
                 ('v', 'A'): ['>^A', '^>A'], ('v', '<'): ['<A'], ('v', 'v'): ['A'], ('v', '>'): ['>A'],
                 ('>', '^'): ['^<A', '<^A'], ('>', 'A'): ['^A'], ('>', '<'): ['<<A'], ('>', 'v'): ['<A'],
                 ('>', '>'): ['A']}


# move maps from movmap.py

def find_shortest_strings(strings):
    min_length = min(len(s) for s in strings)
    return [s for s in strings if len(s) == min_length]


class Pad:

    def __init__(self, name, pad, moves, controller=None):
        self.name = name
        self.pad = pad
        self.moves = moves
        self.controller = controller
        self.current_char = 'A'
        # self.index_A = [(index, row.index('A')) for index, row in enumerate(self.pad) if 'A' in row][0]

    def do_type(self, chars):
        # Calculate which commands I need to enter {chars}
        all_commands_needed = []
        for char in chars:
            commands_needed_for_char = self.moves[(self.current_char, char)]
            all_commands_needed.append(commands_needed_for_char)
            self.current_char = char

        all_commands_needed = [''.join(sequence) for sequence in itertools.product(*all_commands_needed)]

        # print(f"{self.name}\tGot {len(all_commands_needed)} options of length {len(all_commands_needed[0])}\t"
        #       f"{'' if len(all_commands_needed) > 10 else all_commands_needed}")
        # input()

        # Pass to controlling robot
        if self.controller is not None:
            controller_commands = []
            for command in all_commands_needed:
                controller_commands_for_command = self.controller.do_type(command)
                # print(f"{self.name} received {controller_commands_for_command=}")
                controller_commands.append(controller_commands_for_command)
            return find_shortest_strings(controller_commands)
        else:
            return all_commands_needed[0]  # since they are same length, return just one


@aoc_timed_solution(2024, 21, 1)
def run_part1(filename):
    codes = read_to_array(filename)
    dir_robot2 = Pad('dir_robot2', DIR_PAD, DIR_PAD_MOVES)
    dir_robot1 = Pad('dir_robot1', DIR_PAD, DIR_PAD_MOVES, dir_robot2)
    num_robot = Pad('num_robot', NUM_PAD, NUM_PAD_MOVES, dir_robot1)

    count = 0

    for code in codes:
        print(f"### {code} ###")
        commands_needed = num_robot.do_type(code)
        shortest = find_shortest_strings(commands_needed)
        print(f"Final = {shortest=}\n{len(shortest)=}, {len(shortest[0])=}, {len(shortest[0][0])=}")
        count += len(shortest[0][0]) * int(code[:-1])
    return count


@aoc_timed_solution(2024, 21, 2)
def run_part2(filename):
    pass


if __name__ == '__main__':
    run_part1("example_1.txt")
    # run_part1("input.txt")
    # run_part2("example_1.txt")
    # run_part2("input.txt")
