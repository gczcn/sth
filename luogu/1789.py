n, m, k = map(int, input().split())
l = [0 for _ in range(n * n)]
for i in range(m + k):
    x, y = map(int, input().split())
    l[y * n - n + x - 1] = 1
    if y - 1 > 0: l[y * n - 2 * n + x - 1] = 1
    if y - 2 > 0: l[y * n - 3 * n + x - 1] = 1
    if y + 1 <= n: l[y * n + x - 1] = 1
    if y + 2 <= n: l[y * n + n + x - 1] = 1
    if x - 1 > 0: l[y * n - n + x - 2] = 1
    if x - 2 > 0: l[y * n - n + x - 3] = 1
    if x + 1 <= n: l[y * n - n + x] = 1
    if x + 2 <= n: l[y * n - n + x + 1] = 1
    if x - 1 > 0 and y - 1 > 0: l[y * n - 2 * n + x - 2] = 1
    if x + 1 <= n and y - 1 > 0: l[y * n - 2 * n + x] = 1
    if x - 1 > 0 and y + 1 <= n: l[y * n + x - 2] = 1
    if x + 1 <= n and y + 1 <= n: l[y * n + x] = 1
    if i >= m:
        if x - 2 > 0 and y - 1 > 0: l[y * n - 2 * n + x - 3] = 1
        if x + 2 <= n and y - 1 > 0: l[y * n - 2 * n + x + 1] = 1
        if x - 2 > 0 and y + 1 <= n: l[y * n + x - 3] = 1
        if x + 2 <= n and y + 1 <= n: l[y * n + x + 1] = 1
        if x - 2 > 0 and y - 2 > 0: l[y * n - 3 * n + x - 3] = 1
        if x + 2 <= n and y - 2 > 0: l[y * n - 3 * n + x + 1] = 1
        if x - 2 > 0 and y + 2 <= n: l[y * n + n + x - 3] = 1
        if x + 2 <= n and y + 2 <= n: l[y * n + n + x + 1] = 1
        if x - 1 > 0 and y - 2 > 0: l[y * n - 3 * n + x - 2] = 1
        if x + 1 <= n and y - 2 > 0: l[y * n - 3 * n + x] = 1
        if x - 1 > 0 and y + 2 <= n: l[y * n + n + x - 2] = 1
        if x + 1 <= n and y + 2 <= n: l[y * n + n + x] = 1  
print(n * n - sum(l))
