from util.decorators import aoc_solution


@aoc_solution(2023, 5, 1)
def run_part1(filename):
    with open(filename) as file:
        seeds_map = []
        map_text = []
        for i, line in enumerate(file):
            line = line.rstrip()
            if i == 0:
                seeds_map = _insert_seeds(line)
                print(f'Reading seeds {seeds_map}')
            if line == '' and i != 1:
                seeds_map = _append_map_to_seeds_map(seeds_map, map_text)
                map_text = []
            elif line != '' and line[0].isdigit():
                map_text.append(line.rstrip())
        seeds_map = _append_map_to_seeds_map(seeds_map, map_text)
    print(f'Seeds map {seeds_map}')
    return min([seed[-1] for seed in seeds_map])


def _insert_seeds(line):
    return [[int(seed)] for seed in line.split(":")[1].split()]


def _append_map_to_seeds_map(seeds_map, text):
    mapped_values = []
    for seed_list in seeds_map:
        item = seed_list[-1]
        # print(f'For item {item}')
        for line in text:
            values = [int(i) for i in line.split()]
            # print(f'{item} checking {values}')
            index = _find_index(range(values[1], values[1] + values[2]), item)
            if index is not None:
                # print(f'{item} in {list(range(values[1], values[1] + values[2]))}')
                new_val = range(values[0], values[0] + values[2])[index]
                mapped_values.append(new_val)
                # print(f'Adding {new_val} to item {item}')
                break
        else:
            mapped_values.append(item)
    for i, value in enumerate(mapped_values):
        # print(f'Adding {value} to seed {seeds_map[i][0]}')
        seeds_map[i].append(value)
    return seeds_map


def _find_index(arr, item):
    try:
        return arr.index(item)
    except ValueError:
        return None


if __name__ == "__main__":
    run_part1("example_1.txt")
    run_part1("input.txt")
