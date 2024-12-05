from functools import cmp_to_key

from util.decorators import aoc_timed_solution
from util.reader import read_to_array


def create_rule(order_rules, before, after):
    for x in [before, after]:
        if x not in order_rules:
            order_rules[x] = {"before": set(), "after": set()}
    order_rules[before]["after"].add(after)
    order_rules[after]["before"].add(before)
    return order_rules


def is_update_ordered_correctly(order_rules, number, befores, afters, ret='bool'):
    if number not in order_rules:
        return True
    rule_befores = order_rules[number]["before"]
    rule_afters = order_rules[number]["after"]
    if any(after in rule_befores for after in afters) or any(before in rule_afters for before in befores):
        return False if ret == 'bool' else number
    return True if ret == 'bool' else -1


@aoc_timed_solution(2024, 5, 1)
def run_part1(filename):
    data = read_to_array(filename)
    doing_ordering_rules = True
    order_rules = {}
    correct_updates = 0
    for line in data:
        if doing_ordering_rules:
            if line == '':
                doing_ordering_rules = False
                continue
            # Looping ordering rules
            before, after = map(int, line.split('|'))
            order_rules = create_rule(order_rules, before, after)
        else:
            # Looping updates
            update = [int(i) for i in line.split(',')]
            for i in range(len(update)):
                current = update[i]
                befores = update[0: max(i - 1, 0)]
                afters = update[i + 1: len(update)]
                if not is_update_ordered_correctly(order_rules, current, befores, afters):
                    break
            else:
                correct_updates += update[int(len(update) / 2)]
    return correct_updates


def custom_sort(order_rules, update):
    def compare(a, b):
        if a not in order_rules or b not in order_rules:
            return 0
        if a in order_rules[b]["before"]:
            return -1
        if a in order_rules[b]["after"]:
            return 1
        return 0

    return sorted(update, key=cmp_to_key(compare))


@aoc_timed_solution(2024, 2, 2)
def run_part2(filename):
    data = read_to_array(filename)
    doing_ordering_rules = True
    order_rules = {}
    correct_updates = 0
    for line in data:
        if doing_ordering_rules:
            if line == '':
                doing_ordering_rules = False
                continue
            # Looping ordering rules
            before, after = map(int, line.split('|'))
            order_rules = create_rule(order_rules, before, after)
        else:
            # Looping updates
            update = [int(i) for i in line.split(',')]
            for i in range(len(update)):
                current = update[i]
                befores = update[0: max(i - 1, 0)]
                afters = update[i + 1: len(update)]
                if not is_update_ordered_correctly(order_rules, current, befores, afters):
                    sorted_update = custom_sort(order_rules, update)
                    correct_updates += sorted_update[int(len(sorted_update) / 2)]
                    break
    return correct_updates


if __name__ == "__main__":
    run_part1("example_1.txt")  # 143
    run_part1("input.txt")
    run_part2("example_1.txt")  # 123
    run_part2("input.txt")
