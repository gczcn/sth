# n, d = int(input()), []
# for i in range(n):
#     l = input().split()
#     b = float(l[0])
#     for j in range(1, int(l[1]) + 1):
#         a = int(j * b)
#         if a in d: d.remove(a)
#         else: d.append(a)
# print(d[0])
n, l = int(input()), []
for i in range(n):
    l.append(input().split())

