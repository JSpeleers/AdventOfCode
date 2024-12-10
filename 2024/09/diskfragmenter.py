from util.decorators import aoc_timed_solution
from util.reader import read_to_array


def format(diskmap):
    _id = 0
    formatted_diskmap = []
    for i in range(len(diskmap)):
        if diskmap[i] != 0:
            if i % 2 == 0:
                formatted_diskmap.append([_id, diskmap[i]])
                _id += 1
            else:
                formatted_diskmap.append([".", diskmap[i]])
    return formatted_diskmap


def get_last_file_index(formatted_diskmap):
    for i in range(len(formatted_diskmap) - 1, -1, -1):
        if formatted_diskmap[i][0] != "." and formatted_diskmap[i][1] != 0:
            return i
    return None


def get_last_file_indexes(formatted_diskmap):
    # Same as above but in a list
    return [i for i in range(len(formatted_diskmap) - 1, -1, -1) if
            formatted_diskmap[i][0] != "." and formatted_diskmap[i][1] != 0]


def rearrange(formatted_diskmap):
    rearranged_diskmap = []
    lf_count, index_last_file = 0, None
    for i, (char, count) in enumerate(formatted_diskmap):
        if char != ".":
            rearranged_diskmap.append((char, count))
        else:
            while count != 0:
                if lf_count == 0:
                    index_last_file = get_last_file_index(formatted_diskmap)
                    lf_char, lf_count = formatted_diskmap[index_last_file]
                if index_last_file is not None and index_last_file < i:
                    return rearranged_diskmap

                if count <= lf_count:
                    lf_count -= count
                    formatted_diskmap[index_last_file][1] = lf_count
                    rearranged_diskmap.append((lf_char, count))
                    count = 0
                else:
                    formatted_diskmap[index_last_file][1] = 0
                    rearranged_diskmap.append((lf_char, lf_count))
                    count -= lf_count
                    lf_count = 0
    return rearranged_diskmap


def get_first_empty_block(formatted_diskmap, lf_count):
    for i, (char, count) in enumerate(formatted_diskmap):
        if char == '.' and count >= lf_count:
            return i
    return None


def reformat(formatted_diskmap):
    new_formatted_diskamp = []
    count = 0
    for i in range(len(formatted_diskmap)):
        if formatted_diskmap[i][0] == '.':
            count += formatted_diskmap[i][1]
        else:
            if count > 0:
                new_formatted_diskamp.append(['.', count])
                count = 0
            new_formatted_diskamp.append(formatted_diskmap[i])
    if count > 0:
        new_formatted_diskamp.append(['.', count])
    return new_formatted_diskamp


def block_rearrange(formatted_diskmap):
    i = len(formatted_diskmap) - 1
    while i >= 0:
        lf_char, lf_count = formatted_diskmap[i]
        if lf_char != '.':
            index = get_first_empty_block(formatted_diskmap, lf_count)
            if index is not None and index < i:
                char, count = formatted_diskmap[index]
                if count == lf_count:
                    formatted_diskmap[index][0] = lf_char
                    formatted_diskmap[i][0] = '.'
                else:  # count > lf_count
                    formatted_diskmap[i][0] = '.'
                    formatted_diskmap[index][1] = count - lf_count
                    formatted_diskmap.insert(index, [lf_char, lf_count])
                    continue
                formatted_diskmap = reformat(formatted_diskmap)
        i -= 1
    return formatted_diskmap


def expand(rearranged_diskmap):
    expanded_arr = []
    for char, count in rearranged_diskmap:
        expanded_arr += [char] * count
    return expanded_arr


def run(filename, method):
    data = [int(x) for x in read_to_array(filename)[0]]
    formatted_diskmap = format(data)
    rearranged_diskmap = method(formatted_diskmap)
    expanded_rearranged_diskmap = expand(rearranged_diskmap)
    return sum([i * int(x) for i, x in enumerate(expanded_rearranged_diskmap) if x != '.'])


@aoc_timed_solution(2024, 9, 1)
def run_part1(filename):
    return run(filename, rearrange)


@aoc_timed_solution(2024, 9, 2)
def run_part2(filename):
    return run(filename, block_rearrange)


if __name__ == "__main__":
    run_part1("example_1.txt")  # 1928
    run_part1("input.txt")
    run_part2("example_1.txt")  # 2858
    run_part2("input.txt")
