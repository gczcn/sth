# TODO: ...
N = int(input())
m = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
l = []
cp = []
r = []
while True:
    iy, ix, iv = input().split()
    if iy == ix == iv == '0':
        break
    iy, ix, iv = int(iy), int(ix), int(iv)
    m[iy][ix] = iv
    l.insert(0, [iy, ix, iv])
