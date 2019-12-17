import numpy as np
from math import gcd


def moon_energy(moon_pos, moon_vel):
    return np.sum(np.abs(moon_pos))*np.sum(np.abs(moon_vel))


def read_input():
    pos_list = []
    with open('inputs/input12.txt', 'r') as f:
        line = f.readline()
        while line:
            pos_list.append([int(line[(line.find('x') + 2):(line.find(','))]),
                             int(line[(line.find('y') + 2):(line[line.find('y'):].find(',') + line.find('y'))]),
                             int(line[(line.find('z') + 2):(line.find('>'))])])
            line = f.readline()
    return np.array(pos_list)


def update_pos_axis(moons_pos, moons_vel, ax):
    moons_pos[:, ax] = moons_pos[:, ax] + moons_vel[:, ax]
    return moons_pos, moons_vel


def update_vel_axis(moons_pos, moons_vel, ax):
    for i in range(len(moons_pos)):
        for j in range(len(moons_pos)):
            if i != j:
                moons_vel[i, ax] = moons_vel[i, ax] if moons_pos[i, ax] == moons_pos[j, ax] else (
                    moons_vel[i, ax] - 1 if moons_pos[i, ax] > moons_pos[j, ax] else moons_vel[i, ax] + 1)
    return moons_pos, moons_vel


def update_pos(moons_pos, moons_vel):
    moons_pos = moons_pos + moons_vel
    return moons_pos, moons_vel


def update_vel(moons_pos, moons_vel):
    for i in range(len(moons_pos)):
        for j in range(len(moons_pos)):
            if i != j:
                moons_vel[i, 0] = moons_vel[i, 0] if moons_pos[i, 0] == moons_pos[j, 0] else (
                    moons_vel[i, 0] - 1 if moons_pos[i, 0] > moons_pos[j, 0] else moons_vel[i, 0] + 1)
                moons_vel[i, 1] = moons_vel[i, 1] if moons_pos[i, 1] == moons_pos[j, 1] else (
                    moons_vel[i, 1] - 1 if moons_pos[i, 1] > moons_pos[j, 1] else moons_vel[i, 1] + 1)
                moons_vel[i, 2] = moons_vel[i, 2] if moons_pos[i, 2] == moons_pos[j, 2] else (
                    moons_vel[i, 2] - 1 if moons_pos[i, 2] > moons_pos[j, 2] else moons_vel[i, 2] + 1)
    return moons_pos, moons_vel


def print_pos_vel(pos, vel):
    for p, v in zip(pos, vel):
        print(f"pos=<x={p[0]}, y={p[1]}, z={p[2]}>, vel=<x={v[0]}, y=\t{v[1]}, z={v[2]}>")


def day12():
    moons_pos = read_input()
    moons_vel = np.zeros((len(moons_pos), 3), dtype=int)

    for i in range(1000):
        moons_pos, moons_vel = update_vel(moons_pos, moons_vel)
        moons_pos, moons_vel = update_pos(moons_pos, moons_vel)
    # print_pos_vel(moons_pos, moons_vel)
    print(sum([moon_energy(p, v) for p, v in zip(moons_pos, moons_vel)]))

def day12_star():
    moons_pos = read_input()
    moons_vel = np.zeros((len(moons_pos), 3), dtype=int)

    for i in range(3):
        moon_pos_x = moons_pos[:, i]
        moon_vel_x = moons_vel[:, i]
        p_pos = [moon_pos_x.copy()]
        p_vel = [moon_vel_x.copy()]
        end, steps = False, 0

        while not end:
            moons_pos, moons_vel = update_vel_axis(moons_pos, moons_vel, i)
            moons_pos, moons_vel = update_pos_axis(moons_pos, moons_vel, i)
            moon_pos_x = moons_pos[:, i]
            moon_vel_x = moons_vel[:, i]
            steps += 1

            cosa1 = np.nonzero(np.all(np.array(p_pos) == moon_pos_x, axis=1))
            cosa2 = np.nonzero(np.all(np.array(p_vel) == moon_vel_x, axis=1))

            if np.any(np.isin(cosa1, cosa2)):
                end = True
            else:
                p_pos.append(moon_pos_x.copy())
                p_vel.append(moon_vel_x.copy())
        print(steps)
