l, c = list(map(int, input().split())), 0
N, l = l[0], l[1:]
for i in range(len(l)):
    if l[i] == 0: continue
    for _ in range(l[i]):
        print('0' if i % 2 == 0 else '1', end = '')
        c += 1
        if c == N:
            print()
            c = 0
