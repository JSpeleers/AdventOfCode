def run_part1(filename, red, green, blue):
    with open(filename) as file:
        games_map = [_get_max_cubes_of_games(game_string) for game_string in file]
        print(games_map)
    count = 0
    for i, game in enumerate(games_map):
        if game['red'] <= red and game['green'] <= green and game['blue'] <= blue:
            count += i + 1
    return count


def run_part2(filename):
    with open(filename) as file:
        games_map = [_get_max_cubes_of_games(game_string) for game_string in file]
        print(games_map)
    count = 0
    for i, game in enumerate(games_map):
        count += game['red'] * game['blue'] * game['green']
    return count


def _get_max_cubes_of_games(game_string):
    print(f'GAME: {game_string}')
    max_map = {'red': 0, 'green': 0, 'blue': 0}
    for set_string in game_string[game_string.index(':') + 2:].split(';'):
        set_map = _parse_set_string(set_string)
        max_map['red'] = max(max_map['red'], set_map['red'])
        max_map['green'] = max(max_map['green'], set_map['green'])
        max_map['blue'] = max(max_map['blue'], set_map['blue'])
    return max_map


def _parse_set_string(string):
    colors = {'red': 0, 'green': 0, 'blue': 0}
    # print(f'SET {string}')
    for color in string.split(','):
        # print(f'\t{color}')
        set_result = color.strip().split(' ')
        colors[set_result[1]] += int(set_result[0])
    return colors


if __name__ == "__main__":
    print(run_part1('example_1.txt', 12, 13, 14))
    # print(run_part2('example_1.txt'))
    # print(run_part1('input.txt', 12, 13, 14))
    # print(run_part2('input.txt'))
