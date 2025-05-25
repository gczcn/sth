pixels = input()
N = len(pixels)
r = [0]
for _ in range(N - 1):
    pixels = pixels + input()
for _ in range(len(pixels)):
    if pixels[0] == ('0' if (len(r) + 1) % 2 == 0 else '1'):
        r[len(r) - 1] += 1
    else:
        r.append(1)
    pixels = pixels[1:]
print(N, end = '')
for v in r:
    print(' ' + str(v), end = '')
