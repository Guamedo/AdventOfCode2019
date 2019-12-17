from utils import *

def day7():
    with open('inputs/input7.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]

    max_out = -1
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    for m in range(5):
                        sig_array = [i, j, k, l, m]
                        if len(sig_array) == len(set(sig_array)):
                            out = 0
                            for s in sig_array:
                                out, _, _ = execute_program(program.copy(), input_list=[s, out], out_mode=1)
                            max_out = max_out if max_out > out else out
    print(max_out)


# Not working
def day7_star():
    with open('inputs/input7.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]

    amplifiers_p = [program.copy() for _ in range(5)]
    amplifiers_i = [0 for _ in range(5)]

    sig_array = [9, 7, 8, 5, 6]
    last_e = -1
    out, index = 0, 0
    while out != 99 or index < 4:
        out, amplifiers_p[index], amplifiers_i[index] = execute_program(amplifiers_p[index],
                                                                        input_list=[sig_array[index], out],
                                                                        start_index=amplifiers_i[index], out_mode=1)
        last_e = last_e if index != 4 else (out if out != 99 else last_e)
        index = (index + 1) % 5
    print(last_e)