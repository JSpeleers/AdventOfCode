def run_part1(filename):
    with open(filename) as file:
        text = [line.rstrip() for line in file]
    count = 0
    for i in range(len(text)):
        j = 0
        print()
        print(text[i])
        while j < len(text[i]):
            c = text[i][j]
            if c.isdigit():
                coords = _get_coords_of_number(text, i, j)
                print(f'Coords: {coords}')
                adj_coords = _get_adjacent_coords(coords)
                print(f'Adj Coords: {adj_coords}')
                adj_text = _coords_to_text(text, adj_coords)
                print(f'Adj Text: {adj_text}')
                if _contains_symbol(adj_text):
                    print(f'Contains symbol! {adj_text}')
                    count += int(_coords_to_text(text, coords))
                j += len(coords)
            else:
                j += 1
    return count


def _get_coords_of_number(text, x, y):
    coords = []
    c = text[x][y]
    try:
        while c.isdigit():
            coords.append((x, y))
            y += 1
            c += text[x][y]
    except IndexError:
        pass
    finally:
        return coords


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


def _contains_symbol(text):
    return len([c for c in text if not c.isdigit() and c != '.']) > 0


def _coords_to_text(text, coords):
    return ''.join([_try_slice_text(text, coord[0], coord[1]) for coord in coords])


def _try_slice_text(text, x, y):
    try:
        return text[x][y]
    except IndexError:
        return ''


if __name__ == "__main__":
    # print(run_part1('example_1.txt'))
    print(run_part1('input.txt'))
