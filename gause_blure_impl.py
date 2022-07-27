import numpy as np


def gaussian_blur(a: np.ndarray):
    """ Remove noise """
    cols = (a.shape[0] - 3) + 1
    rows = (a.shape[1] - 3) + 1

    lst = np.empty((cols, rows), dtype="int32")

    for i in range(0, cols):
        for j in range(0, rows):
            lst[i, j] = (np.sum(a[i: i + 3, j: j + 3]) // 9)

    return lst
