n = int(input())
l, u = [0], []
for i in range(1, n + 1):
    l.append(l[i - 1] + sum(list(map(int, input().split()))) - 8)
print(sum(l))
