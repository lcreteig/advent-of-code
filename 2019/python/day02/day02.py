#!/usr/bin/env python3


def intcoder(int_prog):
    idx = 0
    while True:
        opcode = int_prog[idx]
        if opcode == 99:
            return int_prog
        elif opcode == 1 or opcode == 2:
            pos1 = int_prog[idx + 1]
            pos2 = int_prog[idx + 2]
            new_pos = int_prog[idx + 3]
            if opcode == 1:
                int_prog[new_pos] = int_prog[pos1] + int_prog[pos2]
            elif opcode == 2:
                int_prog[new_pos] = int_prog[pos1] * int_prog[pos2]
        else:
            raise ValueError(f"Encountered value of {opcode}, which is not 1, 2 or 99")
        idx += 4


def find_input(int_prog, output):
    for noun in range(100):
        for verb in range(100):
            int_prog_new = int_prog.copy()  # reset to original list
            int_prog_new[1:3] = [noun, verb]
            if intcoder(int_prog_new)[0] == output:
                return noun, verb


if __name__ == "__main__":
    with open("input_day02") as f:
        int_prog = [int(_) for _ in f.read().split(",")]
    # Part 1
    int_prog1202 = int_prog.copy()  # keep original list
    int_prog1202[1:3] = [12, 2]
    print("Part 1:", intcoder(int_prog1202)[0])
    # Part 2
    noun, verb = find_input(int_prog, 19690720)
    print("Part 2:", 100 * noun + verb)
