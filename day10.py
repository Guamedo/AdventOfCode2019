import numpy as np
import math

def get_best_pos(pos_list):
    cont_max, best_index = -1, [-1, -1]
    for i, p0 in enumerate(pos_list):
        cont, angle_list = 0, []
        for j, p1 in enumerate(pos_list):
            if i != j:
                y, x = p1 - p0
                angle = math.atan2(y, x)
                if not (angle in angle_list):
                    angle_list.append(angle)
                    cont += 1
        if cont > cont_max:
            cont_max = cont
            best_index = p0.copy()
    return cont_max, best_index


def day10():
    with open('inputs/input10.txt') as f:
        test = np.array([[1 if e=='#' else 0 for e in l] for l in f.read().split('\n')])
    pos_list = np.array(np.argwhere(test == 1))

    out, _ = get_best_pos(pos_list)
    print(out)


def angle_map(angle, start_angle):
    angle = angle - start_angle if angle >= 0 else 2 * math.pi + angle - start_angle
    angle = angle if angle >= 0 else 2 * math.pi + angle
    return 2.*math.pi - angle


# Pues na otro que funciona sin que sepa muy bien como (NO TOCAR)
def day10_star():
    y = 0
    pos_list = []
    with open('inputs/input10.txt') as f:
        line = f.readline()
        while line:
            x = 0
            for c in line:
                if c == '#':
                    pos_list.append([x, y])
                x += 1
            line = f.readline()
            y -= 1
    pos_list = np.array(pos_list)

    cont_max = -1
    cont_max_index = [-1, -1]
    for i, p0 in enumerate(pos_list):
        cont = 0
        angle_list = []
        for j, p1 in enumerate(pos_list):
            if i != j:
                vec = p1-p0
                angle = math.atan2(vec[1], vec[0])
                if not(angle in angle_list):
                    angle_list.append(angle)
                    cont += 1
            if cont > cont_max:
                cont_max = cont
                cont_max_index = p0

    angle_list = []
    dist_list = []
    index_list = []
    for j, p1 in enumerate(pos_list):
        if p1[0] != cont_max_index[0] or p1[1] != cont_max_index[1]:
            vec = p1 - cont_max_index
            dist = math.sqrt(vec[0]**2 + vec[1]**2)
            angle = angle_map(math.atan2(vec[1], vec[0]), start_angle=math.pi/2.)
            if not(angle in angle_list):
                angle_list.append(angle)
                dist_list.append(dist)
                index_list.append(p1.copy())
            else:
                index = np.argwhere(np.array(angle_list) == angle)[0, 0]
                if dist_list[index] > dist:
                    dist_list[index] = dist
                    index_list[index] = p1.copy()
    angle_list = np.array(angle_list)
    index_list = np.array(index_list)

    asteroid_200 = (index_list[np.argsort(angle_list)[198]])
    print(asteroid_200[0]*100-asteroid_200[1])
