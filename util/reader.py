def read_to_array(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def read_to_2d_array(filename):
    with open(filename) as file:
        return [list(line.strip()) for line in file]
