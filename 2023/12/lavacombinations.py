from util.decorators import aoc_timed_solution


def _read_input(filename):
    with open(filename) as file:
        text = []
        for i, line in enumerate(file):
            text.append([])
            for c in line.rstrip():
                text[i].append(c)
    return text


@aoc_timed_solution(2023, 12, 1)
def run_part1(filename, new=False):
    count = 0
    with open(filename) as file:
        for line in file:
            this_count = count_possible_combinations(line.split()[0], [int(i) for i in line.split()[1].split(',')], new)
            print(f'{this_count} combinations for {line.split()[0]} - {[int(i) for i in line.split()[1].split(",")]}')
            count += this_count
    return count


def count_possible_combinations(record, groups, new=False):
    combinations = _generate_combinations(record)
    count = 0
    if new:
        for combination in combinations:
            count += 1 if _is_equal_to(groups, combination) else 0

    else:
        for combination in combinations:
            count += 1 if groups == _get_groups_of_combination(combination) else 0
    return count


def _generate_combinations(record):
    return [
        record.replace('?', '{}').format(*bin(i)[2:].zfill(record.count('?')).replace('0', '.').replace('1', '#'))
        for i in range(2 ** record.count('?'))]


def _get_groups_of_combination(combination):
    return [len(x) for x in combination.split('.') if x != '']


def _is_equal_to(expected, combination):
    current_group_length = 0
    index = 0

    print(f'\nChecking if {combination} groups is {expected}')

    try:
        for char in combination:
            print(f'Got {char} ({current_group_length})')
            if char == '#':
                current_group_length += 1
                print('Adding length')
            elif current_group_length > 0:
                if expected[index] != current_group_length:
                    print(f'FALSE - Got group {current_group_length} and that is not equal to index {index} = {expected[index]}')
                    return False
                else:
                    print(f'Equal, continuing')
                    current_group_length = 0
                    index += 1



        print(f'Ended loop on ({current_group_length}) and {index} and {len(expected)}')
        if current_group_length == 0 and index == len(expected):
            print(f'TRUE - group is 0 at the end')
            return True
        elif expected[index] != current_group_length and index + 1 != len(expected):
            print(f'FALSE - Got group {current_group_length} and that is not equal to {index} = {expected[index]} (end)')
            return False

    except IndexError:
        print(f'FALSE IndexErr')
        return False

    print(f'TRUE - loop done')
    return True


@aoc_timed_solution(2023, 12, 2)
def run_part2(filename):
    count = 0
    with open(filename) as file:
        for line in file:
            record = ((line.split()[0] + '?') * 5)[:-1]
            groups = [int(i) for i in line.split()[1].split(',')] * 5
            this_count = count_possible_combinations(record, groups)
            print(f'{this_count} combinations for {record} - {groups}')
            count += this_count
    return count


if __name__ == "__main__":
    # run_part1("example_1.txt")  # 21
    # run_part1("example_1.txt", new=True)  # 21
    # run_part1("example_1.2.txt")  # 4
    run_part1("example_1.6.txt")  # 10
    run_part1("example_1.6.txt", new=True)  # 10
    # run_part1("input.txt")
    # run_part2("example_1.txt") # 525152
    # run_part2("input.txt")
