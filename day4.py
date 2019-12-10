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