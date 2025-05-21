L, R = input().split()
c = 0
for i in range(0, len(R)):
    c += (10 ** i) * (int(R) // (10 ** (i + 1)) - int(L) // (10 ** (i + 1))) + \
         max(0, min(10 ** i, int(R) % (10 ** (i + 1)) - 2 * 10 ** i + 1)) - \
         max(0, min(10 ** i, int(L) % (10 ** (i + 1)) - 2 * 10 ** i))
print(c)
