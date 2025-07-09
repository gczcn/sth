s = input().split(';')[0:-1]
a = b = c = 0
for i in s:
    exec(i[0] + '=' + i[-1])
print(a, b, c)
