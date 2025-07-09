s, l = input(), 0
for i in range(len(s)):
    if (s[i] == '(' and ')' not in s[i + 1:]) or (s[i] == ')' and '(' not in s[0:i]):
        print('NO')
        exit()

    l += 1 if s[i] == '(' else (-1 if s[i] == ')' else 0)
print('YES' if l == 0 else 'NO')
