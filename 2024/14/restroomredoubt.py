import re

from util.decorators import aoc_timed_solution

pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"


def read(filename):
    with open(filename) as file:
        input_string = file.read()
    return [[(int(x1), int(y1)), (int(x2), int(y2))] for y1, x1, y2, x2 in re.findall(pattern, input_string)]


def mul_count_quadrants(robots, rows, cols):
    mid_row = rows // 2
    mid_col = cols // 2
    print(robots)
    q1 = [robot for robot in robots if robot[0][0] < mid_row and robot[0][1] < mid_col]  # Top left
    q2 = [robot for robot in robots if robot[0][0] < mid_row and robot[0][1] > mid_col]  # Top right
    q3 = [robot for robot in robots if robot[0][0] > mid_row and robot[0][1] < mid_col]  # bottom left
    q4 = [robot for robot in robots if robot[0][0] > mid_row and robot[0][1] > mid_col]  # bottom right
    return len(q1) * len(q2) * len(q3) * len(q4)


def visualize(robots, rows, cols):
    poss = [robots[x][0] for x in range(len(robots))]
    for r in range(rows):
        for c in range(cols):
            if (count := poss.count((r, c))) > 0:
                print(count, end='')
            else:
                print(' ', end='')
        print()


def simulate(robots, rows, cols, count):
    poss = [robots[x][0] for x in range(len(robots))]
    string = [['#' if (r, c) in poss else ' ' for c in range(cols)] for r in range(rows)]

    with open("example_output.txt", 'a') as f:
        f.write(f"----------------------------\n{count=}")
        for s in string:
            f.write(''.join(s) + '\n')


@aoc_timed_solution(2024, 14, 1)
def run_part1(filename, rows, cols, seconds=100):
    robots = read(filename)
    visualize(robots, rows, cols)
    for robot in robots:
        pos_r, pos_c = robot[0]
        d_r, d_c = robot[1]
        new_pos_r = (pos_r + d_r * seconds) % rows
        new_pos_c = (pos_c + d_c * seconds) % cols
        robot[0] = (new_pos_r, new_pos_c)
    print('############################################################')
    visualize(robots, rows, cols)
    return mul_count_quadrants(robots, rows, cols)


@aoc_timed_solution(2024, 14, 2)
def run_part2(filename, rows, cols):
    robots = read(filename)
    visualize(robots, rows, cols)
    counter = 0
    while counter < 10000:
        for robot in robots:
            pos_r, pos_c = robot[0]
            d_r, d_c = robot[1]
            new_pos_r = (pos_r + d_r * 1) % rows
            new_pos_c = (pos_c + d_c * 1) % cols
            robot[0] = (new_pos_r, new_pos_c)
        simulate(robots, rows, cols, counter)
        counter += 1
    return counter


if __name__ == '__main__':
    run_part1("example_1.txt", 7, 11)
    run_part1("input.txt", 103, 101)
    # run_part2("example_1.txt", 7, 11)
    # run_part2("input.txt", 103, 101) # Look at logs.txt
