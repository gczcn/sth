n, k = input().split()
n, k = int(n), int(k)
l = 0
c = 0
while n != 0 or l >= k:
    n -= 1
    c += 1
    l += 1
    if l >= k:
        n += 1
        l -= k
print(c)
