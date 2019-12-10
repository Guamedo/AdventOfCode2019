def day6():
    d = {}
    out = -1
    # No se por que pero funciona
    with open('inputs/input6.txt', 'r') as f:
        for line in f:
            f_line = line.replace('\n', '').split(')')
            if not(f_line[0] in d):
                d[f_line[0]] = 0
            d[f_line[1]] = d[f_line[0]] + 1

    while(out != sum(d.values())):
        out = sum(d.values())
        with open('inputs/input6.txt', 'r') as f:
            for line in f:
                f_line = line.replace('\n', '').split(')')
                if not (f_line[0] in d):
                    d[f_line[0]] = 0
                d[f_line[1]] = d[f_line[0]] + 1
    print(out)


def day6_star():
    d1, d2 = {}, {}

    with open('inputs/input6.txt', 'r') as f:
        for line in f:
            f_line = line.replace('\n', '').split(')')
            d1[str(f_line[1])] = str(f_line[0])
            if not(str(f_line[0])) in d2:
                d2[str(f_line[0])] = []
            d2[str(f_line[0])].append(str(f_line[1]))

    visited = ['YOU']
    keys = [(d1['YOU'], 0)]
    while len(keys) > 0 and keys[0][0] != 'SAN':
        if keys[0][0] in d1 and not(d1[keys[0][0]] in visited):
            visited.append(d1[keys[0][0]])
            keys.append((d1[keys[0][0]], keys[0][1]+1))

        if keys[0][0] in d2:
            for k in d2[keys[0][0]]:
                if not(k in visited):
                    visited.append(k)
                    keys.append((k, keys[0][1]+1))
        keys.pop(0)
    print(keys[0][1]-1)