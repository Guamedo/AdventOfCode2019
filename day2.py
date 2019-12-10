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