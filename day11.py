from utils import execute_program
import numpy as np


def day11():
    with open('inputs/input11.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]
    program = program + [0 for _ in range(len(program) + 100)]

    index = 0
    out, index = execute_program(program, input_list=[0], start_index=index, out_mode=1)
    print(out)
    out, index = execute_program(program, input_list=[0], start_index=index, out_mode=1)
    print(out)
    out, index = execute_program(program, input_list=[0], start_index=index, out_mode=1)
    print(out)
    out, index = execute_program(program, input_list=[0], start_index=index, out_mode=1)
    print(out)


def day11_star():
    pass