K, c = int(input()), 0
for i in range(10000, 30001):
    I = str(i)
    if int(I[0] + I[1] + I[2]) % K == 0 and int(I[1] + I[2] + I[3]) % K == 0 and int(I[2] + I[3] + I[4]) % K == 0:
        print(i)
        c = 1
if c == 0:
    print('No')
