from util.decorators import aoc_timed_solution


@aoc_timed_solution(2023, 12, 1)
def run_part1(filename, new=False): # Brute force
    count = 0
    with open(filename) as file:
        for line in file:
            this_count = count_possible_combinations(line.split()[0], [int(i) for i in line.split()[1].split(',')], new)
            # print(f'{this_count} combinations for {line.split()[0]} - {[int(i) for i in line.split()[1].split(",")]}')
            count += this_count
    return count


def count_possible_combinations(record, groups, new=False):
    expected_amount = sum(groups)
    combinations = _generate_combinations(record)
    print(f'Got {len(combinations)} combinations')
    count = 0
    if new:
        for combination in combinations:
            count += 1 if _is_equal_to(groups, expected_amount, combination) else 0

    else:
        for combination in combinations:
            count += 1 if groups == _get_groups_of_combination(combination) else 0
    return count


def _generate_combinations(record):
    qs = record.count('?')
    r = record.replace('?', '{}')
    return [r.format(*bin(i)[2:].zfill(qs).replace('0', '.').replace('1', '#')) for i in range(2 ** qs)]


def _get_groups_of_combination(combination):
    return [len(x) for x in combination.split('.') if x != '']


def _is_equal_to(expected, expected_amount, combination):
    if expected_amount != combination.count('#'):
        return False

    current_group_length = 0
    index = 0

    try:
        for char in combination:
            if char == '#':
                current_group_length += 1
            elif current_group_length > 0:
                if expected[index] != current_group_length:
                    return False
                else:
                    current_group_length = 0
                    index += 1
        if current_group_length == 0 and index == len(expected):
            return True
        elif expected[index] != current_group_length and index + 1 != len(expected):
            return False
    except IndexError:
        return False
    return True


@aoc_timed_solution(2023, 12, 2)
def run_part2(filename, new=False):
    count = 0
    with open(filename) as file:
        for line in file:
            record = ((line.split()[0] + '?') * 5)[:-1]
            groups = [int(i) for i in line.split()[1].split(',')] * 5
            this_count = count_possible_combinations(record, groups, new)
            print(f'{this_count} combinations for {record} - {groups}')
            count += this_count
    return count


if __name__ == "__main__":
    # run_part1("example_1.txt")  # 21
    # run_part1("example_1.txt", new=True)  # 21
    # run_part1("example_1.6.txt")  # 10
    # run_part1("example_1.6.txt", new=True)  # 10
    # run_part1("input.txt")
    # run_part1("input.txt", new=True)
    run_part2("example_1.1.txt")  # 1
    run_part2("example_1.1.txt", new=True)  # 1
    # run_part2("example_1.2.txt")  # 16384
    # run_part2("example_1.2.txt", new=True)  # 16384
    # run_part2("example_1.4.txt")  # 10
    # run_part2("example_1.4.txt", new=True)  # 10
    # run_part2("example_1.5.txt") # 2500
    # run_part2("example_1.5.txt", new=True)  # 2500
    # run_part2("example_1.txt") # 525152
    # run_part2("input.txt")
