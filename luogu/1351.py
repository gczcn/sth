n, l, t, lst = int(input()), {}, 0, 0
for _ in range(n - 1):
    i = input().split()
    u, v = int(i[0]), int(i[1])
    l[u] = l.get(u, []) + [v]
    l[v] = l.get(v, []) + [u]
W = list(map(int, input().split()))
for i in range(1, n + 1):
    for j in l[i]:
        if j in l:
            for k in l[j]:
                if k > i:
                    c = W[i - 1] * W[k - 1]
                    t += 2 * c
                    if c > lst: lst = c
print(lst, t % 10007)
