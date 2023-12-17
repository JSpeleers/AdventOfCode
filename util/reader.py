def read_to_array(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def read_to_2d_array(filename, _type=str):
    with open(filename) as file:
        return [[_type(i) for i in line.strip()] for line in file]
