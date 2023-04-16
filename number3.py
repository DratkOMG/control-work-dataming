import numpy as np

d = 0.8
# ma3 = np.array([[1, 1, 1, 0, 0, 0, 0],
#                 [0, 0, 0, 1, 1, 0, 0],
#                 [0, 0, 0, 0, 0, 1, 1],
#                 [0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0]])

print("Please enter the number of nodes for lesson 3:")
m3 = int(input())
mat3 = np.zeros((m3, m3), dtype=int)
mat3[0][0] = 1
for i in range(m3):
    if i * 2 + 2 <= m3:
        mat3[i][i * 2 + 1] = 1
        mat3[i][i * 2 + 2] = 1
print(mat3)

pr = [1] * m3


def cal_pagerank(s2):
    return (1 - d) + d * s2


for a in range(10):
    for i in range(len(mat3)):
        s = 0
        col = [row[i] for row in mat3]
        for j in range(len(col)):
            if col[j] == 1:
                s += pr[j] / sum(mat3[j])

        pr[i] = cal_pagerank(s)

print([round(num, 3) for num in pr])
