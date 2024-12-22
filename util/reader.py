def read_to_array(filename, _type=str):
    with open(filename) as file:
        return [_type(line.strip()) for line in file]


def read_strip_to_2d_array(filename, _type=str):
    with open(filename) as file:
        return [[_type(i) for i in line.strip()] for line in file]


def read_split_to_2d_array(filename, _type=str, remove_ws=False):
    with open(filename) as file:
        return [[_type(i) for i in line.split() if i != ' ' or not remove_ws] for line in file]
