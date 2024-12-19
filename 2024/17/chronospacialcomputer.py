from util.decorators import aoc_timed_solution

WALL = "#"
SPACE = "."


def read(filename):
    with open(filename) as file:
        lines = file.readlines()
    return (
        int(lines[0].strip().split(" ")[2]),
        int(lines[1].strip().split(" ")[2]),
        int(lines[2].strip().split(" ")[2]),
        [int(x) for x in lines[4].strip().split(" ")[1].split(",")],
    )


def combo(operand, reg_A, reg_B, reg_C):
    return [0, 1, 2, 3, reg_A, reg_B, reg_C][operand]


def adv(operand, reg_A, reg_B, reg_C, out):
    # Opcode 0: Division of A register by 2^operand, result stored in A register
    return reg_A // (2 ** combo(operand, reg_A, reg_B, reg_C)), reg_B, reg_C, None


def bxl(operand, reg_A, reg_B, reg_C, out):
    # Opcode 1: Bitwise XOR of register B and the instruction's literal operand
    return reg_A, reg_B ^ operand, reg_C, None


def bst(operand, reg_A, reg_B, reg_C, out):
    # Opcode 2: Value of its operand operand modulo 8, then writes that value to the B register
    return reg_A, combo(operand, reg_A, reg_B, reg_C) % 8, reg_C, None


def jnz(operand, reg_A, reg_B, reg_C, out):
    # Opcode 3: If A register is not zero, set instruction pointer to the value of its literal operand
    if reg_A != 0:
        return reg_A, reg_B, reg_C, operand
    return reg_A, reg_B, reg_C, None


def bxc(operand, reg_A, reg_B, reg_C, out):
    # Opcode 4: Bitwise XOR of register B and register C, then stores the result in register B
    return reg_A, reg_B ^ reg_C, reg_C, None


def out(operand, reg_A, reg_B, reg_C, out):
    # Opcode 5: Value of its operand operand modulo 8, then outputs that value
    o = combo(operand, reg_A, reg_B, reg_C) % 8
    if P2_sol[len(out)] != o:
        raise ValueError
    out.append(o)

    # if not qe2(0, P2_sol, out):
    #     raise ValueError
    return reg_A, reg_B, reg_C, None


def bdv(operand, reg_A, reg_B, reg_C, out):
    # Opcode 6: Division of A register by 2^operand, result stored in B register
    return reg_A, reg_A // (2 ** combo(operand, reg_A, reg_B, reg_C)), reg_C, None


def cdv(operand, reg_A, reg_B, reg_C, out):
    # Opcode 7: Division of A register by 2^operand, result stored in C register
    return reg_A, reg_B, reg_A // (2 ** combo(operand, reg_A, reg_B, reg_C)), None


OPS = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


@aoc_timed_solution(2024, 17, 1)
def run_part1(filename):
    out = []
    reg_A, reg_B, reg_C, program = read(filename)

    i = 0
    while i < len(program):
        reg_A, reg_B, reg_C, d_i = OPS[program[i]](
            program[i + 1], reg_A, reg_B, reg_C, out
        )
        if d_i is not None:
            i = d_i
        else:
            i += 2
    return ",".join(out)


@aoc_timed_solution(2024, 17, 2)
def run_part2(filename):
    out = []
    _, og_reg_B, og_reg_C, og_program = read(filename)
    length = len(og_program)
    a = int('1' + ('0' * (length - 1)))  # A has as many digits as the program
    while out != og_program:
        # while a < 1000000001000000:
        a += 1
        reg_A, reg_B, reg_C, out = a, og_reg_B, og_reg_C, []
        i = 0
        # print(a)
        try:
            while i < length:
                reg_A, reg_B, reg_C, d_i = OPS[og_program[i]](
                    og_program[i + 1], reg_A, reg_B, reg_C, out
                )
                i = d_i if d_i is not None else i + 2
        except ValueError:
            continue
        # print(f"{a=} {','.join(out)}")
    return a


if __name__ == "__main__":
    # run_part1("example_1.txt")  # 4,6,3,5,6,3,5,2,1,0
    # run_part1("input.txt")
    P2_sol = [0, 3, 5, 4, 3, 0]
    run_part2("example_2.txt")  # 117440
    # P2_sol = [2, 4, 1, 3, 7, 5, 0, 3, 1, 4, 4, 7, 5, 5, 3, 0]
    # run_part2("input.txt")
