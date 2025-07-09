N = int(input())
l = [[0 for i in range(1001)] for j in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    for j in range(N):
        if j == i:
            continue
        l[j][a:b] = [1 for i in range(b - a)]
max = 0
for i in range(N):
    max = sum(l[i]) if sum(l[i]) > max else max
print(max)
