import math

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