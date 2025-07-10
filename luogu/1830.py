n, m, x, y = map(int, input().split())
l, r = [], []
for _ in range(x):
    x1, y1, x2, y2 = map(int, input().split())
    l.append([[x1, y1], [x2, y2]])
for _ in range(y):
    r.append([0, 0, 0])
    a, b = map(int, input().split())
    for i in range(len(l)):
        if l[i][0][0] <= a <= l[i][1][0] and l[i][0][1] <= b <= l[i][1][1]:
            r[-1][0] = 1
            r[-1][1] += 1
            r[-1][2] = i + 1
for i in r:
    print(f'Y {i[1]} {i[2]}' if i[0] else 'N')
