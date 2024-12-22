from collections import defaultdict

from util.decorators import aoc_timed_solution
from util.reader import read_to_array


def calc(numb):
    for factor in [64, 0.03125, 2048]:  # == 1/32
        numb ^= int(numb * factor) % 16777216
        numb %= 16777216
    return numb


@aoc_timed_solution(2024, 22, 1)
def run_part1(filename, iters):
    secret_numbers = read_to_array(filename, _type=int)
    total = 0
    for numb in secret_numbers:
        new_numb = numb
        for i in range(iters):
            new_numb = calc(new_numb)
        total += new_numb
    return total


@aoc_timed_solution(2024, 22, 2)
def run_part2(filename, iters):
    secret_numbers = read_to_array(filename, _type=int)
    buyers_prices = defaultdict(lambda: 0)
    for s, numb in enumerate(secret_numbers):
        new_numb = numb
        this_buyers_price = dict()

        prices_arr = [int(str(new_numb := calc(new_numb))[-1]) for _ in range(iters)]
        delta_prices_arr = [prices_arr[i] - prices_arr[i - 1] for i in range(1, len(prices_arr))]

        for i in range(4, len(prices_arr)):
            key = ",".join(map(str, delta_prices_arr[i - 4:i]))
            if key not in this_buyers_price:
                this_buyers_price[key] = prices_arr[i]

        for key in this_buyers_price:
            buyers_prices[key] += this_buyers_price[key]

    return max(buyers_prices.values())


if __name__ == '__main__':
    run_part1("example_1.txt", 10)  # 5908254
    run_part1("example_2.txt", 2000)  # 37327623
    run_part1("input.txt", 2000)
    run_part2("example_1.txt", 10)  # 6
    run_part2("example_3.txt", 2000)  # 23
    run_part2("input.txt", 2000)
