import numpy as np


def intersection_point(s1p1, s1p2, s2p1, s2p2):
    x1, y1 = s1p1
    x2, y2 = s1p2

    x3, y3 = s2p1
    x4, y4 = s2p2

    det = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if det == 0:
        return

    t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/det
    u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/det

    if not(0.0 <= t <= 1.0) or not(0.0 <= u <= 1.0):
        return

    return [x1 + t*(x2-x1), y1 + t*(y2-y1)]


def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return np.abs(x1 - x2) + np.abs(y1 - y2)


def execute_program(program, input_list=None, start_index=0, out_mode=0):
    index, input_index, r_base = start_index, 0, 0
    op_code = str(program[index])
    op_code = op_code if len(op_code) == 5 else f"{'0' * (5 - len(op_code))}{op_code}"
    while int(op_code[-2:]) != 99:
        if int(op_code[-2:]) == 1:  # ADD
            p1 = program[program[index + 1]] if op_code[2] == '0' else (
                program[index + 1] if op_code[2] == '1' else program[program[index + 1] + r_base])
            p2 = program[program[index + 2]] if op_code[1] == '0' else (
                program[index + 2] if op_code[1] == '1' else program[program[index + 2] + r_base])
            program[program[index + 3] + (0 if op_code[0] != '2' else r_base)] = p1 + p2
            index += 4
        elif int(op_code[-2:]) == 2:  # MULTIPLY
            p1 = program[program[index + 1]] if op_code[2] == '0' else (
                program[index + 1] if op_code[2] == '1' else program[program[index + 1] + r_base])
            p2 = program[program[index + 2]] if op_code[1] == '0' else (
                program[index + 2] if op_code[1] == '1' else program[program[index + 2] + r_base])
            program[program[index + 3] + (0 if op_code[0] != '2' else r_base)] = p1*p2
            index += 4
        elif int(op_code[-2:]) == 3:  # INPUT
            program[program[index + 1] + (0 if op_code[2] != '2' else r_base)] = int(input("Input: ")) if (input_list is None) else input_list[input_index]
            input_index += 1
            index += 2
        elif int(op_code[-2:]) == 4:  # OUTPUT
            out = program[program[index + 1]] if op_code[2] == '0' else (
                program[index + 1] if op_code[2] == '1' else program[program[index + 1] + r_base])
            index += 2
            if out_mode == 0:
                print(f"Output: {out}")
            else:
                return out, index
        elif int(op_code[-2:]) == 5:  # JUMP IF TRUE
            p1 = program[program[index + 1]] if op_code[2] == '0' else (
                program[index + 1] if op_code[2] == '1' else program[program[index + 1] + r_base])
            p2 = program[program[index + 2]] if op_code[1] == '0' else (
                program[index + 2] if op_code[1] == '1' else program[program[index + 2] + r_base])
            index = p2 if p1 != 0 else index + 3
            pass
        elif int(op_code[-2:]) == 6:  # JUMP IF FALSE
            p1 = program[program[index + 1]] if op_code[2] == '0' else (
                program[index + 1] if op_code[2] == '1' else program[program[index + 1] + r_base])
            p2 = program[program[index + 2]] if op_code[1] == '0' else (
                program[index + 2] if op_code[1] == '1' else program[program[index + 2] + r_base])
            index = p2 if p1 == 0 else index + 3
        elif int(op_code[-2:]) == 7:  # LESS
            p1 = program[program[index + 1]] if op_code[2] == '0' else (
                program[index + 1] if op_code[2] == '1' else program[program[index + 1] + r_base])
            p2 = program[program[index + 2]] if op_code[1] == '0' else (
                program[index + 2] if op_code[1] == '1' else program[program[index + 2] + r_base])
            program[program[index + 3] + (0 if op_code[0]!='2' else r_base)] = 1 if p1 < p2 else 0
            index += 4
        elif int(op_code[-2:]) == 8:  # EQUAL
            p1 = program[program[index + 1]] if op_code[2] == '0' else (
                program[index + 1] if op_code[2] == '1' else program[program[index + 1] + r_base])
            p2 = program[program[index + 2]] if op_code[1] == '0' else (
                program[index + 2] if op_code[1] == '1' else program[program[index + 2] + r_base])
            program[program[index + 3] + (0 if op_code[0] != '2' else r_base)] = 1 if p1 == p2 else 0
            index += 4
        elif int(op_code[-2:]) == 9:  # INCREASE RELATIVE BASE
            r_base += program[program[index + 1]] if op_code[2] == '0' else (
                program[index + 1] if op_code[2] == '1' else program[program[index + 1] + r_base])
            index += 2
        else:
            print(f"ERROR: Unknown operation code ({op_code})")
            break
        op_code = str(program[index])
        op_code = op_code if len(op_code) == 5 else f"{'0' * (5 - len(op_code))}{op_code}"
    return 99, index
