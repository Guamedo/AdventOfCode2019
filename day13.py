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
    ball_pos = [-1, -1]
    paddle_pos = [-1, -1]
    dir_ball = 1

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
        if id == 3:
            paddle_pos = [y, x]

    out = 0
    fg = plt.figure()
    ax = fg.gca()
    h = ax.imshow(greed)
    while out != 99:
        if paddle_pos[1] == ball_pos[1]:
            out, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base,
                                                 input_list=[0], input_mode=1)
        elif paddle_pos[1] > ball_pos[1] + dir_ball and dir_ball !=0:
            out, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base,
                                                 input_list=[-1], input_mode=1)
        elif paddle_pos[1] < ball_pos[1] + dir_ball and dir_ball !=0:
            out, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base,
                                                 input_list=[1], input_mode=1)
        else:
            out, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base,
                                                 input_list=[0], input_mode=1)
        if out == 99:
            break
        if out != 111:
            y, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base)
            if y == 99:
                break
            id, index, r_base = execute_program(program, start_index=index, out_mode=1, start_r_base=r_base)
            if id == 99:
                break
            if out == -1:
                print(f"Score: {id}")
            else:
                greed[y, out] = id
                if id == 4:
                    if out > ball_pos[1]:
                        dir_ball = 1
                    elif out < ball_pos[1]:
                        dir_ball = -1
                    ball_pos = [y, out]
                if id == 3:
                    paddle_pos = [y, out]
        else:
            pass
            h.set_array(greed)
            ax.axis('equal')
            plt.draw()
            plt.pause(1e-20)
    pass