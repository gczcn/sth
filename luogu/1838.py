n, l, c = input().strip(), [i for i in range(2, 11)], [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]] # 这里的 input().strip() 依旧是为防止洛谷逆天的题目数据
for i in range(len(n)): l[int(n[i]) - 1] = i % 2
for i in c:
    if l[i[0]] == l[i[1]] == l[i[2]]:
        print('xiaoa wins.' if l[i[0]] == 0 else 'uim wins.')
        exit()
print('drew.')
