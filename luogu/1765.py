t1 = [' ', 'a', 'd', 'g', 'j', 'm', 'p', 't', 'w']
t2 = ['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x']
t3 = ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y']
t4 = ['s', 'z']
s, c = input(), 0
for i in s:
    if i in t1: c += 1
    if i in t2: c += 2
    if i in t3: c += 3
    if i in t4: c += 4
print(c)
