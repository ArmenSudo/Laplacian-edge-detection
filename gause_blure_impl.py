import numpy as np


def gaussian_blur(img: np.ndarray, kernel: np.ndarray = np.array([[0.0625, 0.125, 0.0625],
                                                                [0.125, 0.25, 0.125],
                                                                [0.0625, 0.125, 0.0625]])):
    """ Remove noise """
    s = 1
    cols = (img.shape[0] - kernel.shape[0]) // s + 1
    rows = (img.shape[1] - kernel.shape[0]) // s + 1

    lst = np.empty((cols, rows), dtype="int32")

    for i in range(0, cols * s, s):
        for j in range(0, rows * s, s):
            lst[i // s, j // s] = (np.sum(img[i: i + kernel.shape[0], j: j + kernel.shape[0]] * kernel))


    return lst
