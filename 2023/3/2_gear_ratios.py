def run_part2(filename):
    with open(filename) as file:
        text = [line.rstrip() for line in file]
    count = 0
    for i in range(len(text)):
        print()
        for j in range(len(text[i])):
            c = text[i][j]
            if _is_gear(c):
                if i - 1 >= 0: print(text[i - 1])
                print(text[i])
                if i + 1 < len(text): print(text[i + 1])
                adj_coords = _get_adjacent_coords([(i, j)])
                print(f'Adj Coords: {adj_coords}')
                print(f'Adj Text: {_coords_to_text(text, adj_coords)}')
                adj_numbers = _get_adjacent_numbers(text, adj_coords)
                print(f'Adj Numbers: {adj_numbers}')
                if len(adj_numbers) == 2:
                    to_add = (adj_numbers.pop() * adj_numbers.pop())
                    count += to_add
                    print(f'Adding {to_add} new count {count}')
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
    return [x[0] for x in set(_get_full_number(text, coord[0], coord[1]) for coord in coords if
                              _try_get_text(text, coord[0], coord[1]).isdigit())]


def _get_full_number(text, x, y):
    c = text[x][y]
    a = 0
    b = 1
    while text[x][y - a: y + b].isdigit() and y - a >= 0:
        c = text[x][y - a: y + b]
        a += 1
    a = max(0, a - 1)
    while text[x][y - a: y + b].isdigit() and y + b <= len(text[x]):
        c = text[x][y - a: y + b]
        b += 1
    b = b - 1 if not y + b < len(text[x]) else b
    return int(c), y - a, y + b


def _coords_to_text(text, coords):
    return ''.join([_try_get_text(text, coord[0], coord[1]) for coord in coords])


def _try_get_text(text, x, y):
    try:
        return '' if x < 0 or y < 0 else text[x][y]
    except IndexError:
        return ''


if __name__ == "__main__":
    # example = run_part2("example_2.txt")
    # print(f'Should be 467835')
    input = run_part2("input.txt")

    # print(f'Example = {example}')
    print(f'Input = {input}')
