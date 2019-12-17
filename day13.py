from utils import execute_program
import matplotlib.pyplot as plt
import numpy as np


def day13():
    with open('inputs/input13.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]
    program = program + [0 for _ in range(len(program) + 100)]

    index, r_base = 0, 0
    x, y, id = 0, 0, 0
    greed = np.zeros((100, 100), dtype=int)

    while x != 99 and y != 99 and id != 99:
        x, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base)
        y, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base)
        id, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base)

    plt.imshow(greed)
    plt.show()


def day13_star():
    pass