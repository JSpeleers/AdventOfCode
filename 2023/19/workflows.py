from util.decorators import aoc_timed_solution


def lt(x, i):
    return x < i


def gt(x, i):
    return x > i


OPS_MAP = {'<': lt, '>': gt}
R_OPS_MAP = {lt: '<', gt: '>'}


class Part:
    def __init__(self, line):
        self.x, self.m, self.a, self.s = [int(x[2:]) for x in line[1:-1].split(',')]

    def __repr__(self):
        return f'(x={self.x},m={self.m},a={self.a},s={self.s})'

    def val(self):
        return self.x + self.m + self.a + self.s


class WorkflowRule:
    def __init__(self, rule):
        if ':' in rule:
            self.prop = rule[0]
            self.ops = OPS_MAP[rule[1]]
            self.val, self.label = rule[2:].split(':')
            self.val = int(self.val)
        else:
            self.ops = None
            self.label = rule

    def __repr__(self):
        if self.ops is None:
            return f'{self.label}'
        return f'{self.prop}{R_OPS_MAP[self.ops]}{self.val}:{self.label}'

    def eval(self, part: Part):
        if self.ops is None:
            return self.label
        return self.label if self.ops(part.__getattribute__(self.prop), self.val) else None

    def _extend_others(self, side, ranged):
        for c in ['x', 'm', 'a', 's']:
            if c != self.prop:
                side[c] = ranged[c]
        return side

    def eval_range(self, ranged):  # Returns range_in, range_out
        if self.ops is None:
            print(f'Returning full range')
            return (self.label, ranged), None
        if self.val in ranged[self.prop]:
            print(f'{ranged} is part of {self}')
            inside = [self.label,
                      {
                          self.prop: (range(ranged[self.prop][0], self.val)) if self.ops == lt else range(self.val, ranged[self.prop][-1] + 1)
                      }]
            inside[1] = self._extend_others(inside[1], ranged)
            outside = {self.prop: [
                range(self.val, ranged[self.prop][-1] + 1) if self.ops == lt else range(ranged[self.prop][-1],
                                                                                        self.val)]}
            outside = self._extend_others(outside, ranged)
            print(f'Inside == {inside}')
            print(f'Outside == {outside}')
            return inside, outside
        return None, ranged


class Workflow:
    def __init__(self, line):
        split = line.split('{')
        self.name = split[0]
        self.rules = [WorkflowRule(rule) for rule in split[1][:-1].split(',')]

    def __repr__(self):
        return f'{self.name}= {[rule for rule in self.rules]}'

    def eval(self, part):
        for rule in self.rules:
            res = rule.eval(part)
            if res is not None:
                return res

    def eval_range(self, ranged):
        ranges = []
        outside = ranged
        for rule in self.rules:
            print(rule)
            if outside is not None:
                inside, outside = rule.eval_range(ranged)
                print(f'from rule {rule} got inside: {inside} and outside {outside}')
                ranges.append(inside)
                ranged = outside
            print(f'Ranges are now {ranges}')
        return ranges


def _read_input(filename):
    started_parts = False
    workflows = dict()
    parts = []
    with open(filename) as file:
        for line in file:
            if (line := line.rstrip()) == '':
                started_parts = True
                continue
            if not started_parts:
                # Read workflows
                workflow = Workflow(line)
                workflows[workflow.name] = workflow
            else:
                parts.append(Part(line))
    return workflows, parts


@aoc_timed_solution(2023, 19, 1)
def run_part1(filename):
    workflows, parts = _read_input(filename)
    return _number_of_accepted_parts(workflows, parts)


def _number_of_accepted_parts(workflows: [Workflow], parts: [Part]):
    count = 0
    for part in parts:
        res = 'in'
        while res != 'A' and res != 'R':
            res = workflows[res].eval(part)
        count += part.val() if res == 'A' else 0
    return count


@aoc_timed_solution(2023, 19, 2)
def run_part2(filename):
    workflows, _ = _read_input(filename)
    return _accepted_ranges(workflows)


def _accepted_ranges(workflows: [Workflow], size=4000):
    finalised_ranges = []
    ranges = [
        ['in', {'x': range(1, size + 1), 'm': range(1, size + 1), 'a': range(1, size + 1), 's': range(1, size + 1)}]]
    while len(ranges) > 0:
        this_range = ranges.pop()
        res_ranges = workflows[this_range[0]].eval_range(this_range[1])
        print('RESULT AFTER 1 WORKFLOW')
        print(res_ranges)
        exit()
        for res_range in res_ranges:
            if res_range[0] == 'A' or res_range[0] == 'R':
                finalised_ranges.append(res_range)
            else:
                ranges.append(res_range)


if __name__ == "__main__":
    run_part1("example_1.txt")  # 19114
    run_part1("input.txt")
    run_part2("example_1.txt")  # 167409079868000
