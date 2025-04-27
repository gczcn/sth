c = []
for i in range(7):
    a = input().split()
    c.append(int(a[0]) + int(a[1]))
if max(c) > 8:
    print(c.index(max(c)) + 1)
else:
    print(0)
