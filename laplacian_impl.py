import numpy as np


def laplacian(a: np.ndarray, b: np.ndarray = np.array([[1, 4, 1],
                                                        [4, -20, 4],
                                                         [1, 4, 1]]), s: int = 1):
    """Laplacian edge detection"""
    cols = (a.shape[0] - b.shape[0]) // s + 1
    rows = (a.shape[1] - b.shape[0]) // s + 1

    lst = np.empty((cols, rows), dtype="int32")

    for i in range(0, cols * s, s):
        for j in range(0, rows * s, s):
            lst[i // s, j // s] = (np.sum(a[i: i + b.shape[0], j: j + b.shape[0]] * b))

    return lst
