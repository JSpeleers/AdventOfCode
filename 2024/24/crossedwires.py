from util.decorators import aoc_timed_solution


def op_and(a, b): return a & b


def op_or(a, b): return a | b


def op_xor(a, b): return a ^ b


OP_MAP = {
    'AND': op_and,
    'OR': op_or,
    'XOR': op_xor
}


def read(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    init_states = {k: int(v) for k, v in (line.split(': ') for line in lines if ': ' in line)}
    wires = [line.strip().split(' ') for line in lines if '->' in line]
    return init_states, wires


def try_wire(states, wire):
    g1, op, g2, _, target = wire
    states[target] = OP_MAP[op](states[g1], states[g2])


@aoc_timed_solution(2024, 24, 1)
def run_part1(filename):
    states, wires = read(filename)
    wires_in_wait = []
    for wire in wires:
        try:
            try_wire(states, wire)
        except KeyError:
            wires_in_wait.append(wire)

    while len(wires_in_wait) > 0:
        wait_len = len(wires_in_wait)
        i = 0
        while i < wait_len:
            try:
                try_wire(states, wires_in_wait[i])
                wires_in_wait.pop(i)
                wait_len -= 1
            except KeyError:
                i += 1

    # print([(key, states[key]) for key in sorted([key for key in states.keys() if key[0] == 'z'], reverse=True)])
    bit_string = [str(states[key]) for key in sorted([key for key in states.keys() if key[0] == 'z'], reverse=True)]
    return int(''.join(bit_string), 2)


@aoc_timed_solution(2024, 24, 2)
def run_part2(filename):
    states, wires = read(filename)
    wires_in_wait = []
    for wire in wires:
        try:
            try_wire(states, wire)
        except KeyError:
            wires_in_wait.append(wire)

    while len(wires_in_wait) > 0:
        wait_len = len(wires_in_wait)
        i = 0
        while i < wait_len:
            try:
                try_wire(states, wires_in_wait[i])
                wires_in_wait.pop(i)
                wait_len -= 1
            except KeyError:
                i += 1

    print([(key, states[key]) for key in sorted([key for key in states.keys() if key[0] == 'z'], reverse=True)])
    bit_string = [str(states[key]) for key in sorted([key for key in states.keys() if key[0] == 'z'], reverse=True)]
    bit_val = int(''.join(bit_string), 2)
    print(f"Result is {bit_string=}")
    expected_bit_string = [str(op_and(states['x' + x], states['y' + x])) for x in ['05', '04', '03', '02', '01', '00']]
    print(f"However, should be {expected_bit_string}")
    return None


if __name__ == '__main__':
    run_part1("example_1.txt")  # 4
    run_part1("example_2.txt")  # 2024
    run_part1("input.txt")
    run_part2("example_3.txt")
    # run_part2("input.txt")
