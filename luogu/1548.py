N, M = map(int, input().split())
s, g = 0, 0
for i in range(N):
    for j in range(M):
        c = (N - i) * (M - j)
        if i == j:
            s += c
        else:
            g += c
print(s, g)
# for i in range(min([N, M])):
#     s += (N - i) * (M - i)
# print(s)
