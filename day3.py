from utils import *

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