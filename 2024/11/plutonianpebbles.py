from collections import defaultdict

from util.decorators import aoc_timed_solution


def read(filename):
    with open(filename) as file:
        return [int(x) for line in file for x in line.split()]


@aoc_timed_solution(2024, 11, 1)
def run_part1(filename, blinks):
    arr = read(filename)
    # Simulating
    for i in range(blinks):
        a = 0
        while a < len(arr):
            if arr[a] == 0:
                arr[a] = 1
                a += 1
            elif len(str(arr[a])) % 2 == 0:
                stone_str = str(arr[a])
                arr[a] = int(stone_str[:int(len(stone_str) / 2)])
                arr.insert(a + 1, int(stone_str[int(len(stone_str) / 2):]))
                a += 2
            else:
                arr[a] *= 2024
                a += 1
    return len(arr)


@aoc_timed_solution(2024, 11, 2)
def run_part2(filename, blinks):
    arrd = {x: 1 for x in read(filename)}
    new_arrd = defaultdict(int)
    # Simulating with caches
    for i in range(blinks):
        for a in arrd:
            if a == 0:
                new_arrd[1] += arrd[0]
            elif (l := len(str(a))) % 2 == 0:
                new_arrd[int(str(a)[:int(l / 2)])] += arrd[a]
                new_arrd[int(str(a)[int(l / 2):])] += arrd[a]
            else:
                new_arrd[a * 2024] += arrd[a]
        arrd = new_arrd
        new_arrd = defaultdict(int)
    return sum(new_arrd[x] for x in new_arrd)


if __name__ == '__main__':
    run_part1("example_1.txt", 6)  # 22
    run_part1("example_1.txt", 25)  # 55312
    run_part1("input.txt", 25)
    run_part2("example_1.txt", 6)  # 22
    run_part2("example_1.txt", 25)  # 55312
    run_part2("input.txt", 25)
    run_part2("input.txt", 75)
