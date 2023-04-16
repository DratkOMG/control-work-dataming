import numpy as np


def calculate_hits(mat, iterations):
    h = np.ones((3, 1), dtype=int)

    mT = np.transpose(mat)

    for i in range(iterations):
        if i != 0:
            h = np.dot(1 / np.amax(La), La)
        lTh = np.dot(mT, h)
        a = np.dot(1 / np.amax(lTh), lTh)
        La = np.dot(mat, a)

    return h, a


matrix = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
])

hub, auth = calculate_hits(matrix, 4)

print(f"hub:\n {hub}")
print(f"authority:\n {auth}")
