n = input().split()
l = int(input()) + 30
c = 0
for i in range(10):
    if int(n[i]) <= l:
        c += 1
print(c)
