from utils import execute_program
import matplotlib.pyplot as plt
import numpy as np


def day11():
    with open('inputs/input11.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]
    program = program + [0 for _ in range(len(program) + 100)]

    index, out, r_base = 0, 0, 0
    painted_pos = []
    white_painted = []
    pos = [0, 0]
    direction = 0

    while out != 99:
        out, index, r_base = execute_program(program, input_list=[1 if pos in white_painted else 0],
                                             start_index=index, out_mode=1, start_r_base=r_base)
        if out == 0:
            if pos in white_painted:
                white_painted.remove(pos)
        else:
            if not (pos in white_painted):
                white_painted.append(pos.copy())
        if not(pos in painted_pos):
            painted_pos.append(pos.copy())

        out, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base)
        direction = (direction - 1 if out == 0 else direction + 1) % 4
        if direction == 0:
            pos[1] += 1
        elif direction == 1:
            pos[0] += 1
        elif direction == 2:
            pos[1] -= 1
        elif direction == 3:
            pos[0] -= 1
        else:
            print(f"ERROR: Unknown direction ({direction})")
    print(len(painted_pos))



def day11_star():
    with open('inputs/input11.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]
    program = program + [0 for _ in range(len(program) + 100)]

    index, out, direction, r_base = 0, 0, 0, 0
    pos = [0, 0]
    white_painted = [pos.copy()]

    while out != 99:
        out, index, r_base = execute_program(program, input_list=[1 if pos in white_painted else 0],
                                             start_index=index, out_mode=1, start_r_base=r_base)
        if out == 0:
            if pos in white_painted:
                white_painted.remove(pos)
        else:
            if not (pos in white_painted):
                white_painted.append(pos.copy())

        out, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base)
        direction = (direction - 1 if out == 0 else direction + 1) % 4
        if direction == 0:
            pos[1] += 1
        elif direction == 1:
            pos[0] += 1
        elif direction == 2:
            pos[1] -= 1
        elif direction == 3:
            pos[0] -= 1
        else:
            print(f"ERROR: Unknown direction ({direction})")

    white_painted = np.array(white_painted)

    plt.plot(white_painted[:, 0], white_painted[:, 1], '*')
    plt.autoscale()
    plt.axis('equal')
    plt.show()