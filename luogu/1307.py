N, A, s = input(), '', 0
if N[0] == '-': N, s = N[1:], 1
for i in range(len(N) - 1, -1, -1):
    A = A + N[i]
print(('-' if s else '') + str(int(A)))
