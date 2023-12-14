from functools import cache

import numpy as np

from util.decorators import aoc_timed_solution


def _read_input(filename):
    with open(filename) as file:
        pattern = []
        for i, line in enumerate(file):
            pattern.append(list(line.strip()))
    return np.array(pattern)


@aoc_timed_solution(2023, 14, 1)
def run_part1(filename):
    arr = _read_input(filename)
    arr_north = _slide_arr_north(arr)
    return _load_on_north_support_beam(arr_north)


@aoc_timed_solution(2023, 14, 2)
def run_part2(filename, cycles):
    arr = _read_input(filename)

    hash_history = []
    value_history = []  # Can be better when not saving all the values
    start_index = None
    cycle_length = 0

    for i in range(cycles):
        arr = _do_cycle(arr)
        arr_hash = _get_hash(arr)
        # print(f'Cycle {i} = {_load_on_north_support_beam(arr)}')

        if arr_hash in hash_history:
            index = hash_history.index(arr_hash)
            if start_index is None:
                # Start loop
                start_index = index
            elif start_index == index:
                # Loop found and ended
                # print(f'Cycle found at start index {start_index} with length {cycle_length}')
                offset = (cycles - start_index - 1) % cycle_length
                # print(f'I need to do {cycles} cycles so that means this is equal to index {start_index + offset}')
                return value_history[start_index + offset]
            cycle_length += 1
        else:
            hash_history.append(arr_hash)
            value_history.append(_load_on_north_support_beam(arr))
            if start_index is not None:
                # Reset current loop
                start_index = None
                cycle_length = 0
    return ValueError


def _get_hash(numpy_arr):  # Find better way to hash
    return ''.join([c for row in numpy_arr for c in row])


def _do_cycle(arr):
    arr = _slide_arr_north(arr)
    arr = _slide_arr_west(arr)
    arr = _slide_arr_south(arr)
    arr = _slide_arr_east(arr)
    return arr


def _slide_arr_north(arr):
    # For each row in transposed array, split by '#' and reorder substring then join again with '#' and transpose back
    return np.array([list('#'.join([_slide_list_west(i) for i in ''.join(row).split('#')])) for row in arr.T]).T


def _slide_arr_east(arr):
    # Flip, slide west, flip again
    return np.flip(_slide_arr_west(np.flip(arr, axis=1)), axis=1)


def _slide_arr_south(arr):
    # Flip, slide north, flip again
    return np.flip(_slide_arr_north(np.flip(arr, axis=0)), axis=0)


def _slide_arr_west(arr):
    # For each row in arr, split by '#' and reorder substring then join again with '#'
    return np.array([list('#'.join([_slide_list_west(i) for i in ''.join(row).split('#')])) for row in arr])


@cache
def _slide_list_west(list_str):
    return 'O' * list_str.count('O') + '.' * list_str.count('.')


def _load_on_north_support_beam(arr):
    count = 0
    for i, row in enumerate(arr):
        count += (len(arr) - i) * ''.join(row).count('O')
    return count


if __name__ == "__main__":
    run_part1("example_1.txt")  # 136
    run_part1("input.txt")
    run_part2("example_1.txt", 1000000000)  # 64
    run_part2("input.txt", 1000000000)
