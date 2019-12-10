import numpy as np
import matplotlib.pyplot as plt

def day8():
    w, h = 25, 6
    with open('inputs/input8.txt', 'r') as f:
        images = f.read()
    i0, i1 = 0, w*h
    min_zero = np.Inf
    out = -1
    while i1 <= len(images):
        image = np.array([int(dig) for dig in images[i0:i1]])
        if np.count_nonzero(image == 0) < min_zero:
            min_zero = np.count_nonzero(image == 0)
            out = np.count_nonzero(image == 1)*np.count_nonzero(image == 2)
        i0 += w*h
        i1 += w*h
    print(out)


def day8_star():
    w, h = 25, 6
    with open('inputs/input8.txt', 'r') as f:
        images = f.read()
    i0, i1 = 0, w*h
    out_image = np.zeros(w*h)+2
    while i1 <= len(images):
        image = np.array([int(dig) for dig in images[i0:i1]])
        out_image[np.argwhere(out_image==2)] = image[np.argwhere(out_image==2)]
        i0 += w*h
        i1 += w*h
    plt.imshow(out_image.reshape((h, w)), cmap='gray')
    plt.show()