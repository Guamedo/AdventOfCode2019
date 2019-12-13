from utils import execute_program
import matplotlib.pyplot as plt
import numpy as np


def day11():
    with open('inputs/input11.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]
    program = program + [0 for _ in range(len(program) + 100)]

    index, out = 0, 0
    painted_pos = []
    white_painted = []
    pos = [0, 0]
    direction = 0
    while out != 99:
        out, index = execute_program(program, input_list=[1 if pos in white_painted else 0], start_index=index, out_mode=1)
        if out == 99:
            break

        if out == 0:
            if pos in white_painted:
                white_painted.remove(pos.copy())
        else:
            if not (pos in white_painted):
                white_painted.append(pos.copy())
        if not(pos in painted_pos):
            painted_pos.append(pos.copy())

        out, index = execute_program(program, start_index=index, out_mode=1)
        direction = (direction - 1 if out == 0 else direction + 1) % 4
        print(out)
        if direction == 0:
            pos[1] += 1
        elif direction == 1:
            pos[0] += 1
        elif direction == 2:
            pos[1] -= 1
        elif direction == 3:
            pos[0] += 1
        else:
            print(f"ERROR: Unknown direction ({direction})")
    print(len(painted_pos))


def day11_star():
    pass