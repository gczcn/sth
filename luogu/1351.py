n, t, lst = int(input()), 0, 0
l = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    l[u].append(v)
    l[v].append(u)
W = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    li = l[i]
    if len(li) >= 2:
        lst = max(lst, max([W[j] for j in li]) * sorted([W[j] for j in li])[-2])
        t = (t + (sum([W[j] for j in li]) ** 2 - sum([W[j] ** 2 for j in li]))) % 10007
print(lst, t)
