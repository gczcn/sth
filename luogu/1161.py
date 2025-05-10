# Need PyPy 3
n, r = int(input()), [False for _ in range(2000001)]
for j in range(n):
    l = input().split()
    for i in range(1, int(l[1]) + 1):
        r[int(i * float(l[0]))] = not r[int(i * float(l[0]))]
print(r.index(True))

# Deepseek:
# n = int(input())
# result = 0
#
# for _ in range(n):
#     a_str, b = input().split()
#     a = float(a_str)
#     b = int(b)
#     for i in range(1, b + 1):
#         result ^= int(i * a)
#
# print(result)
