M, N = map(int, input().split())
s = ''.join(map(str, range(M, N + 1)))
for i in range(10):
    print(('' if i == 0 else ' ') + str(s.count(str(i))), end = '')
