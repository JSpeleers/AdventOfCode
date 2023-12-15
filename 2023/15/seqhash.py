from util.decorators import aoc_timed_solution


@aoc_timed_solution(2023, 15, 1)
def run_part1(filename, only_on=None):
    if only_on is not None:
        return _hash(only_on)

    total_value = 0
    with open(filename) as file:
        for line in file:
            for string in line.split(','):
                total_value += _hash(string)
    return total_value


def _hash(string):
    value = 0
    for c in string:
        value += ord(c)
        value *= 17
        value %= 256
    return value


@aoc_timed_solution(2023, 15, 2)
def run_part2(filename):
    value = 0
    with open(filename) as file:
        for line in file:
            value += _calc_focusing_power(_create_boxes(line.split(',')))
    return value


def _create_boxes(steps):
    boxes = [[] for _ in range(256)]
    for step in steps:
        operation = '-' if '-' in step else '='
        seq_str = step[:step.index(operation)]
        val_str = step[step.index(operation) + 1:]
        box_i = _hash(seq_str)

        if operation == '=':
            for i, (box_seq, box_value) in enumerate(boxes[box_i]):
                if box_seq == seq_str:
                    boxes[box_i][i] = (seq_str, int(val_str))
                    break
            else:
                boxes[box_i].append((seq_str, int(val_str)))

        elif operation == '-':
            for (box_seq, box_value) in boxes[box_i]:
                if box_seq == seq_str:
                    boxes[box_i].remove((box_seq, box_value))
                    break
        # _print_boxes(boxes)
    return boxes


def _calc_focusing_power(boxes):
    value = 0
    for i, box in enumerate(boxes):
        for j, (box_seq, box_value) in enumerate(box):
            value += (i + 1) * (j + 1) * box_value
    return value


def _print_boxes(boxes):
    for i, box in enumerate(boxes):
        if len(box) > 0:
            print(f'Box {i}: {box}')


if __name__ == "__main__":
    run_part1("example_1.txt", only_on="HASH")  # 52
    run_part1("example_1.txt")  # 1320
    run_part1("input.txt")
    run_part2("example_1.txt")  # 145
    run_part2("input.txt")
