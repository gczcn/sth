from functools import reduce
n, S = int(input()), 0
for i in range(1, n + 1):
    S += reduce(lambda x, y: x * y, range(1, i + 1))
