from utils import *


def day9():
    with open('inputs/input9.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]

    program = program + [0 for _ in range(len(program) + 100)]
    execute_program(program, input_list=[1])

def day9_star():
    with open('inputs/input9.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]

    program = program + [0 for _ in range(len(program) + 100)]
    execute_program(program, input_list=[2])