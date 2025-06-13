n, l, c = int(input()), list(map(int, input().split())), [1]
for i in range(1, n):
    if l[i] - l[i - 1] == 1:
        c[-1] += 1
    else:
        c.append(1)
print(max(c))
