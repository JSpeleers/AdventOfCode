from util.decorators import aoc_timed_solution
from util.reader import read_split_to_2d_array


def is_report_safe(report):
    multiplier = -1 if report[0] < report[1] else 1  # decreasing or increasing
    for i in range(len(report) - 1):
        if not 1 <= (report[i] - report[i + 1]) * multiplier <= 3:
            return False
    return True


@aoc_timed_solution(2024, 2, 1)
def run_part1(filename):
    matrix = read_split_to_2d_array(filename, _type=int)
    safe_report_counter = 0
    for report in matrix:
        if is_report_safe(report):
            safe_report_counter += 1
            continue
    return safe_report_counter


@aoc_timed_solution(2024, 2, 2)
def run_part2(filename):
    matrix = read_split_to_2d_array(filename, _type=int)
    safe_report_counter = 0
    for report in matrix:
        if is_report_safe(report):
            safe_report_counter += 1
            continue
        # Check if removing 1 level fixes the issue
        for i in range(len(report)):
            report_cut = report.copy()
            report_cut.pop(i)
            if is_report_safe(report_cut):
                safe_report_counter += 1
                break
    return safe_report_counter


if __name__ == "__main__":
    run_part1("example_1.txt")  # 2
    run_part1("input.txt")  # 559
    run_part2("example_1.txt")  # 4
    run_part2("input.txt")
