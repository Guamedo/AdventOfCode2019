from utils import execute_program
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np


def day13():
    with open('inputs/input13.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]
    program = program + [0 for _ in range(len(program) + 100)]

    index, r_base = 0, 0
    x, y, id = 0, 0, 0
    greed = np.zeros((23, 43), dtype=int)

    while x != 99 and y != 99 and id != 99:
        x, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base)
        if x == 99:
            break

        y, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base)
        if y == 99:
            break

        id, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base)
        if id == 99:
            break

        greed[y, x] = id
        if id == 4:
            ball_pos = [y, x]
    print(np.count_nonzero(greed==2))


def day13_star():
    with open('inputs/input13.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]
    program = program + [0 for _ in range(len(program) + 100)]
    program[0] = 2

    index, r_base = 0, 0
    x, y, id = 0, 0, 0
    greed = np.zeros((23, 43), dtype=int)
    score = 0

    while True:
        x, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base, input_mode=1)
        y, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base, input_mode=1)
        id, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base, input_mode=1)
        if x == -1 and y == 0:
            score = id
            break
        greed[y, x] = id
        if id == 4:
            ball_pos = [y, x]
    plt.imshow(greed)
    plt.show()

    out = 0
    while out != 99:
        out, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base, input_mode=1)

        plt.imshow(greed)
        plt.show()

    pass