import sys

import numpy as np

from util.decorators import aoc_timed_solution


def _read_input(filename):
    with open(filename) as file:
        instructions = [(line.split()[0], int(line.split()[1])) for line in file]
    return instructions


@aoc_timed_solution(2023, 18, 1)
def run_part1(filename):
    instructions = _read_input(filename)
    matrix = _traverse(instructions)
    sections = _build_sections(matrix)
    return _calculate_digsite(sections, len(matrix) - 1, len(matrix[0]) - 1) + np.count_nonzero(matrix == '#')


def _traverse(instructions):
    matrix = np.array([['#']])
    row, col = 0, 0
    for (di, val) in instructions:
        no_rows, no_cols = len(matrix), len(matrix[0])
        print(f'At {(row, col)} with {(no_rows, no_cols)} and got {di, val}')
        # input()

        if di == 'R':
            if col + val + 1 > no_cols:
                cols_to_add = val - (no_cols - col) + 1
                # print(f'Extending right from {no_cols} to {no_cols + cols_to_add} cols: adding {cols_to_add}')
                matrix = np.append(matrix, np.full((no_rows, cols_to_add), '.'), axis=1)
                # simple_print(matrix)
            matrix = _fill_row(matrix, row, col, col + val)
            col += val
            # simple_print(matrix)

        elif di == 'L':
            if col - val < 0:
                # print(f'Extending left from {no_cols} to {no_cols + (val - col)} cols: adding {(val - col)}')
                matrix = np.insert(matrix, [0], np.full((no_rows, val - col), '.'), axis=1)
                col += (val - col)
                # simple_print(matrix)
            matrix = _fill_row(matrix, row, col - val - 1, col)
            col -= val
            # simple_print(matrix)

        elif di == 'U':
            if row - val < 0:
                rows_to_add = val - row
                # print(f'Extending up from {no_rows} to {no_rows + rows_to_add} rows: adding {rows_to_add}')
                matrix = np.insert(matrix, [0], np.full((rows_to_add, no_cols), '.'), axis=0)
                # simple_print(matrix)
                row += rows_to_add
            matrix = _fill_coll(matrix, col, row - val - 1, row)
            row -= val
            # simple_print(matrix)

        elif di == 'D':
            if row + val + 1 > no_rows:
                rows_to_add = val - (no_rows - row) + 1
                # print(f'Extending down from {no_rows} to {no_rows + rows_to_add} rows: adding {rows_to_add}')
                matrix = np.append(matrix, np.full((rows_to_add, no_cols), '.'), axis=0)
                # simple_print(matrix)
            matrix = _fill_coll(matrix, col, row, row + val)
            row += val
            # simple_print(matrix)

        # print()
    return matrix


def _fill_row(matrix, row, start_i, end_i, fill='#'):
    matrix[row][start_i + 1:end_i + 1] = [fill] * (end_i - start_i)
    return matrix


def _fill_coll(matrix, col, start_i, end_i, fill='#'):
    # print(f'{col, start_i, end_i}')
    for i in range(start_i + 1, end_i + 1):
        matrix[i][col] = fill
    return matrix


def _build_sections(matrix):
    section_list = []
    traversed = set()
    for row, line in enumerate(matrix):
        for col, c in enumerate(line):
            if (row, col) not in traversed and c != '#':
                found_section = _build_section(matrix, set(), row, col)
                section_list.append(found_section)
                traversed = traversed.union(found_section)
    return section_list


def _build_section(matrix, traversed, row, col):
    if matrix[row][col] != '#' and (row, col) not in traversed:
        traversed.add((row, col))
        for (n_row, n_col) in _neighbors(matrix, row, col):
            traversed = traversed.union(_build_section(matrix, traversed, n_row, n_col))
    return traversed


def _neighbors(matrix, row, col):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        # Check if the new coordinates are within the matrix boundaries
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            neighbors.append((new_row, new_col))
    return neighbors


def _calculate_digsite(sections, max_row, max_col):
    for section in sections:
        for (row, col) in section:
            if row == 0 or col == 0 or row > max_row or col > max_col:
                break
        else:
            return len(section)


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    run_part1("example_1.txt")  # 62
    run_part1("input.txt")
    # run_part2("example_1.txt")
    # run_part2("input.txt")
