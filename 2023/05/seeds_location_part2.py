from util.decorators import aoc_solution
import sys


@aoc_solution(2023, 5, 2)
def run_part2(filename):
    seed_ranges = None
    translation_maps = []
    # Create translation maps
    print(f'Creating maps')
    with open(filename) as file:
        map_text = []
        for i, line in enumerate(file):
            line = line.rstrip()
            if i == 0:
                seed_ranges = _insert_seed_ranges(line)
            if line == '' and i != 1:
                translation_maps = _append_map_to_translation_maps(translation_maps, map_text)
                map_text = []
            elif line != '' and line[0].isdigit():
                map_text.append(line.rstrip())
    # Loop seeds
    print(f'Looping seeds')
    min_location = sys.maxsize
    for seed_range in seed_ranges:
        print('Next range')
        for seed in seed_range:
            # print(f'SEED: {seed}')
            location = _get_location_of_seed(translation_maps, seed)
            # print(f'Got location {location} for seed {seed}')
            min_location = min(min_location, location)
    return min_location


def _insert_seed_ranges(line):
    arr = [int(seed) for seed in line.split(":")[1].split()]
    return [range(arr[i], arr[i] + arr[i + 1]) for i in range(0, len(arr), 2)]


def _append_map_to_translation_maps(translation_maps, text):
    translation_map = []
    for line in text:
        vals = [int(i) for i in line.split()]
        translation_map.append([vals[1], vals[1] + vals[2], vals[0]])  # source_from, source_to, destination_from
    translation_maps.append(sorted(translation_map))
    return translation_maps


def _get_location_of_seed(translation_maps, seed):
    number = seed
    for translation_map in translation_maps:
        # print(f'Searching for {number}')
        for translation_range in translation_map:
            if translation_range[0] <= number < translation_range[1]:
                # print(f'Found value {number} in between {translation_range[0]} and {translation_range[1]}')
                number = translation_range[2] + number - translation_range[0]
                break
            elif translation_range[0] > number:
                break  # Since ranges are sorted, you can skip other ranges
    return number


if __name__ == "__main__":
    run_part2("example_1.txt")  # 46
    run_part2("input.txt")
