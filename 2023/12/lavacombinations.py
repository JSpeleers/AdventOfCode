from functools import cache

from util.decorators import aoc_timed_solution


def count_possible_combinations(record, groups, new=False):
    return _dynamic_programming_strategy(record, groups) if new else _brute_force_strategy(record, groups)


@aoc_timed_solution(2023, 12, 1)
def run_part1(filename, new=False):  # Brute force
    count = 0
    with open(filename) as file:
        for line in file:
            count += count_possible_combinations(line.split()[0], [int(i) for i in line.split()[1].split(',')], new)
    return count


def _brute_force_strategy(record, groups):
    count = 0
    for combination in _generate_combinations(record):
        count += 1 if groups == _get_groups_of_combination(combination) else 0
    return count


def _generate_combinations(record):
    qs = record.count('?')
    r = record.replace('?', '{}')
    return [r.format(*bin(i)[2:].zfill(qs).replace('0', '.').replace('1', '#')) for i in range(2 ** qs)]


def _get_groups_of_combination(combination):
    return [len(x) for x in combination.split('.') if x != '']


@aoc_timed_solution(2023, 12, 2)
def run_part2(filename, new=True):
    count = 0
    with open(filename) as file:
        for line in file:
            record = ((line.split()[0] + '?') * 5)[:-1]
            groups = [int(i) for i in line.split()[1].split(',')] * 5
            count += count_possible_combinations(record, groups, new)
    return count


def _dynamic_programming_strategy(record, groups):
    return do_dp(tuple(record), tuple(groups), 0, 0, 0)


@cache
def do_dp(record, groups, record_i, group_i, current_count):
    # try:
    #     print(f'Start {record_i}={record[record_i]} - {group_i}={groups[group_i]} - {current_count}')
    # except IndexError:
    #     pass

    if record_i == len(record):  # End reached
        if (group_i == len(groups) and current_count == 0) \
                or (group_i == len(groups) - 1 and groups[group_i] == current_count):
            # Final situation is correct: no busy block and length match OR last block matches
            return 1
        else:
            # Else no match
            return 0
    count = 0
    for c in ['.', '#']:
        if record[record_i] == c or record[record_i] == '?':
            if c == '.' and current_count == 0:
                # No current block, continue
                # print(f'No current block, continuing with {c}')
                count += do_dp(record, groups, record_i + 1, group_i, current_count)
            elif c == '.' and current_count > 0 and group_i < len(groups) and groups[group_i] == current_count:
                # End of expected group
                # print(f'Block has ended')
                count += do_dp(record, groups, record_i + 1, group_i + 1, 0)
            elif c == '#':
                # Count and continue
                # print(f'Found block, counter + 1')
                count += do_dp(record, groups, record_i + 1, group_i, current_count + 1)
    return count


if __name__ == "__main__":
    # run_part1("example_1.txt")  # 21
    # run_part1("example_1.txt", new=True)  # 21
    # run_part1("example_1.6.txt")  # 10
    # run_part1("example_1.6.txt", new=True)  # 10
    run_part1("input.txt")
    run_part1("input.txt", new=True)
    # run_part1("input.txt", new=True)
    # run_part2("example_1.1.txt")  # 1
    # run_part2("example_1.2.txt")  # 16384
    # run_part2("example_1.4.txt")  # 10
    # run_part2("example_1.5.txt") # 2500
    # run_part2("example_1.txt")  # 525152
    run_part2("input.txt")
    # What a ride
