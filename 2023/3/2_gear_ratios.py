def run_part2(filename):
    with open(filename) as file:
        text = [line.rstrip() for line in file]
    count = 0
    for i in range(len(text)):
        print()
        print(text[i])
        for j in range(len(text[i])):
            c = text[i][j]
            if _is_gear(c):
                adj_coords = _get_adjacent_coords([(i, j)])
                print(f'Adj Coords: {adj_coords}')
                print(f'Adj Text: {_coords_to_text(text, adj_coords)}')
                adj_numbers = _get_adjacent_numbers(text, adj_coords)
                print(f'Adj Numbers: {adj_numbers}')
                if len(adj_numbers) == 2:
                    count += adj_numbers.pop() * adj_numbers.pop()
                # exit()
    return count


def _is_gear(char):
    return char == '*'


def _get_adjacent_coords(coords):
    adj_coords = set()
    for coord in coords:
        adj_coords.add((coord[0] - 1, coord[1]))
        adj_coords.add((coord[0] - 1, coord[1] - 1))
        adj_coords.add((coord[0] - 1, coord[1] + 1))
        adj_coords.add((coord[0], coord[1] - 1))
        adj_coords.add((coord[0], coord[1] + 1))
        adj_coords.add((coord[0] + 1, coord[1]))
        adj_coords.add((coord[0] + 1, coord[1] - 1))
        adj_coords.add((coord[0] + 1, coord[1] + 1))
    return adj_coords


def _get_adjacent_numbers(text, coords):
    # TODO filter out duplicates without using a set
    return set(_get_full_number(text, coord[0], coord[1]) for coord in coords if
            _try_get_text(text, coord[0], coord[1]).isdigit())


def _get_full_number(text, x, y):
    c = text[x][y]
    a = 0
    b = 1
    while text[x][y - a: y + b].isdigit() and y - a >= 0:
        c = text[x][y - a: y + b]
        a += 1
    a = max(0, a - 1)
    # a = a - 1 if y - a < 0 else a
    while text[x][y - a: y + b].isdigit() and y + b < len(text[x]):
        c = text[x][y - a: y + b]
        b += 1
    # b = b - 1 if not y + b < len(text[x]) else b
    print(f'FULL: {c} -- {a} vs {b}')
    return int(c)


def _coords_to_text(text, coords):
    return ''.join([_try_get_text(text, coord[0], coord[1]) for coord in coords])


def _try_get_text(text, x, y):
    try:
        return text[x][y]
    except IndexError:
        return ''


if __name__ == "__main__":
    print(f'Result = {run_part2("example_1.txt")}')
    # print(f'Result = {run_part2("input.txt")}')
