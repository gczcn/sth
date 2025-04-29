c, l = input().split(), []
for i in range(1, len(c) - 1):
    l.append(abs(int(c[i]) - int(c[i + 1])))
for i in range(1, len(c) - 1):
    try:
        l.index(i)
    except ValueError:
        print('Not jolly')
        exit()
print('Jolly')
