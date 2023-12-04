from word2number import w2n


def run_part1(filename):
    total_calibration = 0
    with open(filename) as file:
        for line in file:
            first_digit, last_digit = None, None
            for c in line:
                if c.isdigit():
                    first_digit = c if first_digit is None else first_digit
                    last_digit = c
            total_calibration += int(first_digit + last_digit)
            print(first_digit, last_digit, total_calibration)
    return total_calibration


def run_part2(filename):
    total_calibration = 0
    with open(filename) as file:
        for line in file:
            print(line)
            first_digit, last_digit = _find_first_and_last_digit(line)
            total_calibration += int(str(first_digit) + str(last_digit))
            print(first_digit, last_digit, total_calibration)
    return total_calibration


def _find_first_and_last_digit(string):
    first_digit, last_digit = None, None
    i = 0
    length = len(string)
    while i < length:  # Loop all characters
        c = string[i]
        # print(i, c, c.isdigit())
        if c.isdigit():
            first_digit = c if first_digit is None else first_digit
            last_digit = c
            # print('UPDATE', first_digit, last_digit)
        else:
            j = i + 3  # Numbers are at least 3 long
            while j <= length:  # Loop following characters
                substring = string[i: j]
                if any(i.isdigit() for i in substring):  # Skip substring if it contains a digit
                    break
                number_from_word = str(_word_to_number(substring))
                # print('w2n: ', substring, number_from_word)
                if number_from_word is not None and number_from_word.isdigit():
                    first_digit = number_from_word[-1] if first_digit is None else first_digit
                    last_digit = number_from_word[-1]
                    # print('UPDATE', first_digit, last_digit)
                j += 1
        i += 1

    return first_digit, last_digit


def _word_to_number(string):
    # print('w2n: ', string)
    try:
        return w2n.word_to_num(string)
    except ValueError:
        return None


if __name__ == "__main__":
    # print(run_part1('example_1.txt'))
    # print(run_part2('example_2.txt'))
    # print(_find_first_and_last_digit('7pq1rstsixteen'))
    print(run_part2('input.txt'))
