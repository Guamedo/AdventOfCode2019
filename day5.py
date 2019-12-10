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
