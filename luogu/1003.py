n = int(input())
d = [[]]
r = -1
for i in range(n):
    a, b, dx, dy = input().split()
    a, b, dx, dy = int(a), int(b), int(dx), int(dy)
    d.append([a, b, dx, dy])
x, y = input().split()
x, y = int(x), int(y)
for i in range(len(d) - 1, 0, -1):
    xl, xm, yl, ym = d[i][0], d[i][0] + d[i][2], d[i][1], d[i][1] + d[i][3]
    if x >= xl and x <= xm and y >= yl and y <= ym:
        r = i
        break
print(r)
