def run_part1(filename):
    count = 0
    with open(filename) as file:
        for line in file:
            number_of_matches = _get_number_of_matches(line)
            if number_of_matches > 0:
                count += pow(2, number_of_matches - 1)
    return count


def run_part2(filename):
    cards = [1] * sum(1 for _ in open(filename))
    with open(filename) as file:
        for i, line in enumerate(file):
            cards = _add_card_matches(cards, i, _get_number_of_matches(line))
    return sum(cards)


def _get_number_of_matches(line):
    card = line.rstrip().split(':')[1].split('|')
    return len([x for x in card[1].split() if x in card[0].split()])


def _add_card_matches(cards, index, number):
    for i in range(1, number + 1):
        cards[index + i] += cards[index]
    return cards


if __name__ == "__main__":
    print(f'{run_part1("example_1.txt")}')
    print(f'{run_part1("input.txt")}')
    print(f'{run_part2("example_1.txt")}')
    print(f'{run_part2("input.txt")}')
