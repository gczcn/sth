n, l, c = int(input()), list(map(int, input().split())), 0
for i in range(1, n):
    if l[i - 1] > l[i]:
        for j in range(i + 1, n):
            if l[j] < l[i]:
                break
            if l[j] > l[i]:
                c += 1
                break
print(c)
