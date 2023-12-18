def simple_print(arr):
    string = ''
    for line in arr:
        string += ''.join([c for c in line])
        string += '\n'
    print(string)
