from util.decorators import aoc_solution


@aoc_solution(2023, 5, 2)
def run_part2(filename):
    with open(filename) as file:
        puzzle_input = [line for line in file]
    # Create seed and map ranges
    seed_ranges = _get_seed_ranges(puzzle_input[0])
    translation_maps = _get_translation_maps(puzzle_input[3:])
    # print(f'Seed ranges = {seed_ranges}')
    # print(f'Translation maps = {translation_maps}')

    for translation_map in translation_maps:
        i = 0
        while i < len(seed_ranges):
            seed_start, seed_end = seed_ranges[i]
            # print(f'Seed range {seed_ranges[i]}')
            for map_range in translation_map:
                source_start, source_end, destination_start, destination_end, distance = map_range
                if source_start <= seed_start <= source_end:  # Begin of the seed range overlaps
                    # print(f'Seed range {seed_ranges[i]} overlaps in the start with {map_range}')
                    seed_ranges[i][0] = (seed_start - source_start) + destination_start
                    # If end of range is in the translation range: calculate new end - else - add a new seed range
                    if seed_end <= source_end:
                        seed_ranges[i][1] = (seed_end - source_start) + destination_start
                        # print(f'\tMapped to {seed_ranges[i]}')
                    else:
                        seed_ranges[i][1] = destination_end
                        seed_ranges.append([source_end + 1, seed_end])
                        # print(f'\tMapped to {seed_ranges[i]} and added extra seed range of {seed_ranges[-1]}')
                    break
                elif source_end >= seed_end >= source_start:  # End of the seed range overlaps
                    # print(f'Seed range {seed_ranges[i]} overlaps in the end with {map_range}')
                    seed_ranges[i][1] = (seed_end - source_start) + distance
                    if seed_start >= source_start:
                        seed_ranges[i][0] = (seed_start - source_start) + destination_start
                        # print(f'\tMapped to {seed_ranges[i]}')
                    else:
                        seed_ranges[i][0] = destination_start
                        seed_ranges.append([seed_start, source_start - 1])
                        # print(f'\tMapped to {seed_ranges[i]} and added extra seed range of {seed_ranges[-1]}')
                    break
            i += 1
        # print(f'After map: {seed_ranges}\n')
    return min(min(seed_ranges))


def _get_seed_ranges(line):
    arr = [int(seed) for seed in line.split(":")[1].split()]
    return [[arr[i], arr[i] + arr[i + 1] - 1] for i in range(0, len(arr), 2)]  # [seed_start, seed_end]


def _get_translation_maps(map_text):
    maps = []
    current_map = []
    for line in map_text:
        if not line.rstrip():
            continue
        elif line[0].isdigit():
            # [source_start, source_end, destination_start, destination_end, distance]
            vals = [int(i) for i in line.split()]
            current_map.append([vals[1], vals[1] + vals[2] - 1, vals[0], vals[0] + vals[2] - 1, vals[2]])
        else:
            maps.append(sorted(current_map))
            current_map = []
    maps.append(sorted(current_map))
    return maps


if __name__ == "__main__":
    run_part2("example_1.txt")  # 46
    run_part2("input.txt")
