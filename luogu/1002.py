from math import ceil
bx, by, cx, cy = input().split()
bx, by, cx, cy = int(bx), int(by), int(cx), int(cy)
a, cn = [[0, 1, 0]], [bx + by - cx - cy, by - cy + 1]
if cn[0] == 0 :
    print(0)
else:
    cn = [
        cn,
        [cn[0] - 1, cn[1] + 1], [cn[0] - 1, cn[1] - 2],
        [cn[0] + 1, cn[1] + 2], [cn[0] + 1, cn[1] - 1],
        [cn[0] - 3, cn[1] - 1], [cn[0] - 3, cn[1] - 2],
        [cn[0] + 3, cn[1] + 2], [cn[0] + 3, cn[1] + 1],
    ]
    for i in range(1, bx + by):
        a.append([0 for _ in range(i + 3)])
        for j in range(1, i + 2):
            if [i, j] not in cn:
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    print(int(a[len(a) - 1][by]) + int(a[len(a) - 1][by + 1]))
