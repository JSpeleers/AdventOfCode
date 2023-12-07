from collections import Counter
from enum import Enum

from util.decorators import aoc_solution

hand_naming_map = {6: 'Five of a kind', 5: 'Four of a kind', 4: 'Full house', 3: 'Three of a kind', 2: 'Double pair',
                   1: 'Pair', 0: 'High card'}

card_rank_p1 = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1,
                '2': 0}

card_rank_p2 = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1,
                'J': 0}


class Hand(Enum):
    FIVEOFAKIND = 6
    FOUROFAKIND = 5
    FULLHOUSE = 4
    THREEOFAKIND = 3
    DOUBLEPAIR = 2
    PAIR = 1
    HIGHCARD = 0


class HandP1:
    def __init__(self, line):
        self.cards, self.bid = line.split()
        self.bid = int(self.bid)
        self.counts = Counter(self.cards).values()
        self.max_value = max(self.counts)

    def __repr__(self):
        return f'Hand({self.cards}:{self.bid}:{hand_naming_map.get(self.get_hand_value().value)})'

    def __lt__(self, other):
        return [self.get_hand_value().value] + self.get_card_ranks() < [
            other.get_hand_value().value] + other.get_card_ranks()

    def get_card_ranks(self):
        return [card_rank_p1.get(card) for card in self.cards]

    def get_hand_value(self):
        if self.max_value == 5:
            return Hand.FIVEOFAKIND
        elif self.max_value == 4:
            return Hand.FOUROFAKIND
        elif self.max_value == 3:
            if 2 in self.counts:
                return Hand.FULLHOUSE
            else:
                return Hand.THREEOFAKIND
        elif self.max_value == 2:
            if len(self.counts) == 3:
                return Hand.DOUBLEPAIR
            else:
                return Hand.PAIR
        else:
            return Hand.HIGHCARD


class HandP2(HandP1):
    def __init__(self, line):
        super().__init__(line)
        self.counts = Counter([c for c in self.cards if c != 'J']).values()
        self.max_value = max(self.counts) if len(self.counts) > 0 else 0
        self.jokers = self.cards.count('J')

    def get_card_ranks(self):
        return [card_rank_p2.get(card) for card in self.cards]

    def get_hand_value(self):
        if self.max_value == 5 or self.max_value + self.jokers == 5:
            return Hand.FIVEOFAKIND

        elif self.max_value == 4 or self.max_value + self.jokers == 4:
            return Hand.FOUROFAKIND

        elif self.max_value == 3:
            # jokers == 0
            if 2 in self.counts:
                return Hand.FULLHOUSE
            else:
                return Hand.THREEOFAKIND

        elif self.max_value == 2:
            if self.jokers == 1:
                if len(self.counts) == 2:
                    return Hand.FULLHOUSE
                else:
                    return Hand.THREEOFAKIND
            else:
                if len(self.counts) == 3:
                    return Hand.DOUBLEPAIR
                else:
                    return Hand.PAIR

        else:
            if self.jokers == 2:
                return Hand.THREEOFAKIND
            if self.jokers == 1:
                return Hand.PAIR
            else:
                return Hand.HIGHCARD


@aoc_solution(2023, 7, 1)
def run_part1(filename):
    with open(filename) as file:
        return sum([(i + 1) * hand.bid for i, hand in enumerate(sorted([HandP1(line.rstrip()) for line in file]))])


@aoc_solution(2023, 7, 2)
def run_part2(filename):
    with open(filename) as file:
        return sum([(i + 1) * hand.bid for i, hand in enumerate(sorted([HandP2(line.rstrip()) for line in file]))])


if __name__ == "__main__":
    run_part1("example_1.txt")
    run_part1("input.txt")
    run_part2("example_1.txt")
    run_part2("input.txt")
