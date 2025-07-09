n, m = map(int, input().split())
l1, l2 = [], []
for i in range(n):
    l1.append(int(input()))
for i in range(n - m + 1):
    l2.append(sum(l1[i:i + m]))
print(min(l2))
