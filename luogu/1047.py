l, m = input().split()
l, m = int(l), int(m)
f = [1 for i in range(l + 1)]
c = 0
for i in range(m):
    a, b = input().split()
    a, b = int(a), int(b)
    for j in range(b - a + 1):
        if f[a + j] == 1:
            c += 1
            f[a + j] = 0
print(l - c + 1)
