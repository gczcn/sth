N, z = int(input()), []
for i in range(2, N):
    for j in range(2, i):
        if i % j == 0 and i != j: break
    else: z.append(i)
for i in range(2, N + 1, 2):
    for j in z:
        if (i - j) in z:
            print(f'{i}={j}+{i - j}')
            break
