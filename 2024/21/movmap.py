from itertools import permutations


def create_movement_dict(pad):
    coords = {num: (row, col)
              for row, line in enumerate(pad)
              for col, num in enumerate(line) if num is not None}

    def calculate_moves(start_c, end_c):
        start_row, start_col = coords[start_c]
        end_row, end_col = coords[end_c]
        moves = []

        # Vertical
        if end_row > start_row:
            moves.extend(['v'] * (end_row - start_row))
        elif end_row < start_row:
            moves.extend(['^'] * (start_row - end_row))

        # Horizontal
        if end_col > start_col:
            moves.extend(['>'] * (end_col - start_col))
        elif end_col < start_col:
            moves.extend(['<'] * (start_col - end_col))

        # All perms
        return [''.join(p) for p in set(permutations(moves))]

    movement_map = {}
    for start in coords:
        for end in coords:
            movement_map[(start, end)] = [x + 'A' for x in calculate_moves(start, end)]
    return movement_map

# if __name__ == '__main__':
#     NUM_PAD = [[7, 8, 9],
#                [4, 5, 6],
#                [1, 2, 3],
#                [None, 0, 'A']]
#     movement_map = create_movement_dict(NUM_PAD)
#     for key in movement_map.keys():
#         print(f"{key=} = {movement_map[key]}")
#
#     DIR_PAD = [[None, '^', 'A'], ['<', 'v', '>']]
#     movement_map2 = create_movement_dict(DIR_PAD)
#     for key in movement_map2.keys():
#         print(f"{key=} = {movement_map2[key]}")
#     # run_part1("input.txt")
#     # run_part2("example_1.txt")
#     # run_part2("input.txt")
