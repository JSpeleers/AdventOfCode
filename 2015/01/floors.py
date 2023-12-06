from util.decorators import aoc_solution


@aoc_solution(2015, 1, 1)
def run(filename):
    with open(filename) as file:
        return sum([sum([1 if c == '(' else -1 for c in line]) for line in file])


if __name__ == "__main__":
    run('input.txt')
