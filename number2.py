import numpy as np

d = 0.8

# ma2 = np.array([[1, 1, 0, 0, 0],
#                [0, 0, 1, 0, 0],
#                [0, 0, 0, 1, 0],
#                [0, 0, 0, 0, 1],
#                [0, 0, 0, 0, 0]])

# number 2
print("Please enter the number of nodes for lesson 2:")
m2 = int(input())
mat2 = np.zeros((m2, m2), dtype=int)
mat2[0][0] = 1
for i in range(m2):
    if i + 1 < m2:
        mat2[i][i + 1] = 1
print(mat2)

pr = [1] * m2


def cal_pagerank(s2):
    return (1 - d) + d * s2


for a in range(10):
    for i in range(len(mat2)):
        s = 0
        col = [row[i] for row in mat2]
        for j in range(len(col)):
            if col[j] == 1:
                s += pr[j] / sum(mat2[j])

        pr[i] = cal_pagerank(s)

print([round(num, 3) for num in pr])
