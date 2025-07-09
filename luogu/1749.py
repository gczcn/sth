T = int(input())
for i in range(T):
    N, k = map(int, input().split())
    print('No' if N < k / 2 + k ** 2 / 2 else 'Yes')
