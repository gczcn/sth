l, t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', [1, 1]
for i in range(2):
    # 注：此处的 input().strip() 是因为洛谷中题目数据有可能含有 \r 😂
    # 参见：https://www.luogu.com/paste/cb7doh5c
    for j in input().strip():
        t[i] = t[i] * (l.find(j) + 1)
print('GO' if t[0] % 47 == t[1] % 47 else 'STAY')
