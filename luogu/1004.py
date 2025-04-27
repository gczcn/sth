N = int(input())
p, r, b = [[0, 0, 0]], [], {}
while True:
    x, y, n = input().split()
    if x == y == n == '0': break
    x, y, n = int(x), int(y), int(n)
    b[x] = { y: n }
p[0][2] = (b[1][1] if 1 in b and 1 in b[1] else 0)
while len(p) != 0:
    x, y, n = p[0][0], p[0][1], p[0][2]
    if x != N: p.append([x + 1, y, n + (b[x + 1][y] if x + 1 in b and y in b[x + 1] else 0)])
    if y != N: p.append([x, y + 1, n + (b[x][y + 1] if x in b and y + 1 in b[x] else 0)])
    if x == y == N: r.append(n)
    del p[0]
print(m)
