l, b, g = input(), 0, 0
for i in range(len(l)):
    c = l[i]
    if c == '.': continue
    if c == 'b': b += 1; continue
    if c == 'g': g += 1; continue
    if c == 'i' and l[i - 1] != 'g': g += 1; continue
    if c == 'l' and l[i - 1] != 'r' and l[i - 2] != 'i' and l[i - 3] != 'g': g += 1; continue
    if c == 'o' and l[i - 1] != 'b': b += 1; continue
    if c == 'r' and l[i - 1] != 'i' and l[i - 2] != 'g': g += 1; continue
    if c == 'y' and l[i - 1] != 'o' and l[i - 1] != 'b': b += 1; continue
print(b)
print(g)
