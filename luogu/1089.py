c = l = 0
for i in range(12):
    y = int(input())
    if l + 300 - y >= 0:
        c += int((l + 300 - y) / 100)
        l = l + 300 - y - int((l + 300 - y) / 100) * 100
    else:
        print(-i - 1)
        quit()
print(120 * c + l)
