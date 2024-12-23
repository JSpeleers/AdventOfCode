from collections import defaultdict

from util.decorators import aoc_timed_solution


def read(filename):
    with open(filename) as file:
        return [line.strip().split('-') for line in file]


@aoc_timed_solution(2024, 23, 1)
def run_part1(filename):
    network = read(filename)
    lans = defaultdict(set)
    for pc1, pc2 in network:
        lans[pc1].add(pc2)
        lans[pc2].add(pc1)
    threes = set()
    for i in lans:
        for j in lans[i]:
            for k in lans[j]:
                if i in lans[k]:
                    l = [i, j, k]
                    l.sort()
                    threes.add(','.join(l))
    return sum([1 for t in threes if any(pc[0] == 't' for pc in t.split(','))])


@aoc_timed_solution(2024, 23, 2)
def run_part2(filename):
    network = read(filename)
    lans = defaultdict(set)
    for pc1, pc2 in network:
        lans[pc1].add(pc2)
        lans[pc2].add(pc1)
    uniq_pcs = set(lans.keys())

    connected_lans = None
    new_connected_lans = list([x] for x in lans.keys())
    while len(new_connected_lans) > 0:
        connected_lans = new_connected_lans
        # print(connected_lans)
        new_connected_lans = []
        seen = set()
        for cl in connected_lans:
            for pc in [x for x in uniq_pcs if x not in cl]:
                seen_str = ','.join(sorted(cl + [pc]))
                if all(pc in lans[cpc] for cpc in cl) and seen_str not in seen:
                    new_connected_lans.append(sorted(cl + [pc]))
                    seen.add(seen_str)
    return ','.join(connected_lans[0])


if __name__ == '__main__':
    run_part1("example_1.txt")
    run_part1("input.txt")
    run_part2("example_1.txt")
    run_part2("input.txt")
