import math
import numpy as np
import matplotlib.pyplot as plt


def day1():
    with open('inputs/input1.txt', 'r') as f:
        print(sum([int(math.floor(float(n)/3.0) - 2.0) for n in f.read().split('\n')]))


def day1_star():
    with open('inputs/input1.txt', 'r') as f:
        mass_list = [float(n) for n in f.read().split('\n')]

    sum = 0
    for mass in mass_list:
        fuel = int(math.floor(mass/3.0)) - 2
        while fuel >= 0:
            sum += fuel
            fuel = int(math.floor(fuel/3.0)) - 2
    print(sum)


def day2():
    with open('inputs/input2.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]

    program[1] = 12
    program[2] = 2

    index = 0
    while program[index] != 99 :
        if program[index] == 1:
            program[program[index + 3]] = program[program[index+1]] + program[program[index+2]]
        elif program[index] == 2:
            program[program[index + 3]] = program[program[index + 1]]*program[program[index + 2]]
        else:
            print("ERROR")
            break
        index += 4
        if index >= len(program):
            print("ERROR")
            break
    print(program[0])


def day2_star():
    with open('inputs/input2.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]
    program_save = program.copy()

    out_noun = -1
    out_verb = -1
    for noun in range(100):
        for verb in range(100):
            program = program_save.copy()
            program[1] = noun
            program[2] = verb

            index = 0
            while program[index] != 99 :
                if program[index] == 1:
                    program[program[index+3]] = program[program[index+1]] + program[program[index+2]]
                elif program[index] == 2:
                    program[program[index + 3]] = program[program[index + 1]]*program[program[index + 2]]
                else:
                    print("ERROR")
                    break
                index += 4
                if index >= len(program):
                    print("ERROR")
                    break
            if program[0] == 19690720:
                out_verb = verb
                break
        if program[0] == 19690720:
            out_noun = noun
            break
    if out_noun >= 0 and out_verb >= 0:
        print(100*out_noun+out_verb)
    else:
        print("ERROR")


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


def day3():
    with open('inputs/input3.txt', 'r') as f:
        wire1 = [[0, 0]]
        for code in f.readline().split(','):
            dir1 = code[0]
            dist = int(code[1:])
            wire1.append([wire1[-1][0] + (dist if dir1 == "R" else (-dist if dir1 == "L" else 0)),
                          wire1[-1][1] + (dist if dir1 == "U" else (-dist if dir1 == "D" else 0))])

        wire2 = [[0, 0]]
        for code in f.readline().split(','):
            dir2 = code[0]
            dist = int(code[1:])
            wire2.append([wire2[-1][0] + (dist if dir2 == "R" else (-dist if dir2 == "L" else 0)),
                          wire2[-1][1] + (dist if dir2 == "U" else (-dist if dir2 == "D" else 0))])

        wire1 = np.array(wire1)
        wire2 = np.array(wire2)

    min_dist = np.Inf
    for i in range(1, len(wire1) - 1):
        for j in range(1, len(wire2) - 1):
            it = intersection_point(wire1[i], wire1[i + 1], wire2[j], wire2[j + 1])
            if not (it is None):
                m_dist = manhattan_distance(it, [0, 0])
                min_dist = m_dist if m_dist < min_dist else min_dist
    print(min_dist)


def day3_star():
    with open('inputs/input3.txt', 'r') as f:
        wire1 = [[0, 0]]
        for code in f.readline().split(','):
            dir1 = code[0]
            dist = int(code[1:])
            wire1.append([wire1[-1][0] + (dist if dir1 == "R" else (-dist if dir1 == "L" else 0)),
                          wire1[-1][1] + (dist if dir1 == "U" else (-dist if dir1 == "D" else 0))])

        wire2 = [[0, 0]]
        for code in f.readline().split(','):
            dir2 = code[0]
            dist = int(code[1:])
            wire2.append([wire2[-1][0] + (dist if dir2 == "R" else (-dist if dir2 == "L" else 0)),
                          wire2[-1][1] + (dist if dir2 == "U" else (-dist if dir2 == "D" else 0))])

        wire1 = np.array(wire1)
        wire2 = np.array(wire2)

    min_dist = np.Inf
    d_w1 = manhattan_distance(wire1[0], wire1[1])
    for i in range(1, len(wire1)-1):
        d_w2 = manhattan_distance(wire2[0], wire2[1])
        for j in range(1, len(wire2)-1):
            it = intersection_point(wire1[i], wire1[i+1], wire2[j], wire2[j+1])
            if not(it is None):
                d1 = manhattan_distance(wire1[i], it)
                d2 = manhattan_distance(wire2[j], it)
                m_dist = d_w1+d1+d_w2+d2
                min_dist = m_dist if m_dist < min_dist else min_dist
            d_w2 += manhattan_distance(wire2[j], wire2[j+1])
        d_w1 += manhattan_distance(wire1[i], wire1[i + 1])

    print(min_dist)


def day4():
    cont = 0
    for i in range(178416, 676461):
        str_num = str(i)

        cond1 = False
        cond2 = True
        for i in range(len(str_num)-1):
            if str_num[i]==str_num[i+1]:
                cond1 = True
            if int(str_num[i]) > int(str_num[i+1]):
                cond2 = False
                break
        if cond1 and cond2:
            cont += 1
    print(cont)


def day4_star():
    cont = 0
    for j in range(178416, 676461):
        str_num = str(j)

        cond1 = False
        cond2 = True
        for i in range(len(str_num)-1):
            if str_num[i] == str_num[i+1]:
                if i+2 >= len(str_num):
                    if str_num[i-1] != str_num[i]:
                        cond1 = True
                elif str_num[i] != str_num[i+2]:
                    if i-1 < 0:
                        cond1 = True
                    elif str_num[i-1] != str_num[i]:
                        cond1 = True
            if int(str_num[i]) > int(str_num[i+1]):
                cond2 = False
                break
        if cond1 and cond2:
            cont += 1
    print(cont)


def day5():
    with open('inputs/input5.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]

    index = 0
    op_code = str(program[index])
    op_code = op_code if len(op_code) == 5 else f"{'0'*(5-len(op_code))}{op_code}"
    while int(op_code[-2:]) != 99:
        if int(op_code[-2:]) == 1:
            p1 = program[program[index + 1]] if op_code[2] == '0' else program[index + 1]
            p2 = program[program[index + 2]] if op_code[1] == '0' else program[index + 2]
            program[program[index + 3]] = p1 + p2
            index += 4
        elif int(op_code[-2:]) == 2:
            p1 = program[program[index + 1]] if op_code[2] == '0' else program[index + 1]
            p2 = program[program[index + 2]] if op_code[1] == '0' else program[index + 2]
            program[program[index + 3]] = p1*p2
            index += 4
        elif int(op_code[-2:]) == 3:
            program[program[index + 1]] = int(input("Input: "))
            index += 2
        elif int(op_code[-2:]) == 4:
            print(f"Output: {program[program[index + 1]] if op_code[2] == '0' else program[index + 1]}")
            index += 2
        else:
            print(f"ERROR: Unknown operation code ({op_code})")
            break
        op_code = str(program[index])
        op_code = op_code if len(op_code) == 5 else f"{'0' * (5 - len(op_code))}{op_code}"


def day5_star():
    with open('inputs/input5.txt', 'r') as f:
        program = [int(n) for n in f.read().split(',')]

    index = 0
    op_code = str(program[index])
    op_code = op_code if len(op_code) == 5 else f"{'0'*(5-len(op_code))}{op_code}"
    while int(op_code[-2:]) != 99:
        if int(op_code[-2:]) == 1:
            p1 = program[program[index + 1]] if op_code[2] == '0' else program[index + 1]
            p2 = program[program[index + 2]] if op_code[1] == '0' else program[index + 2]
            program[program[index + 3]] = p1 + p2
            index += 4
        elif int(op_code[-2:]) == 2:
            p1 = program[program[index + 1]] if op_code[2] == '0' else program[index + 1]
            p2 = program[program[index + 2]] if op_code[1] == '0' else program[index + 2]
            program[program[index + 3]] = p1*p2
            index += 4
        elif int(op_code[-2:]) == 3:
            program[program[index + 1]] = int(input("Input: "))
            index += 2
        elif int(op_code[-2:]) == 4:
            print(f"Output: {program[program[index + 1]] if op_code[2] == '0' else program[index + 1]}")
            index += 2
        elif int(op_code[-2:]) == 5:
            p1 = program[program[index + 1]] if op_code[2] == '0' else program[index + 1]
            p2 = program[program[index + 2]] if op_code[1] == '0' else program[index + 2]
            index = p2 if p1 != 0 else index + 3
            pass
        elif int(op_code[-2:]) == 6:
            p1 = program[program[index + 1]] if op_code[2] == '0' else program[index + 1]
            p2 = program[program[index + 2]] if op_code[1] == '0' else program[index + 2]
            index = p2 if p1 == 0 else index + 3
        elif int(op_code[-2:]) == 7:
            p1 = program[program[index + 1]] if op_code[2] == '0' else program[index + 1]
            p2 = program[program[index + 2]] if op_code[1] == '0' else program[index + 2]
            program[program[index + 3]] = 1 if p1 < p2 else 0
            index += 4
        elif int(op_code[-2:]) == 8:
            p1 = program[program[index + 1]] if op_code[2] == '0' else program[index + 1]
            p2 = program[program[index + 2]] if op_code[1] == '0' else program[index + 2]
            program[program[index + 3]] = 1 if p1 == p2 else 0
            index += 4
        else:
            print(f"ERROR: Unknown operation code ({op_code})")
            break
        op_code = str(program[index])
        op_code = op_code if len(op_code) == 5 else f"{'0' * (5 - len(op_code))}{op_code}"


if __name__ == "__main__":
    day5_star()