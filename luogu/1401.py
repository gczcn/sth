xl, xu = map(int, input().split())
yl, yu = map(int, input().split())
l = [xl * yl, xu * yu, xl * yu, xu * yl]
print('int' if min(l) >= -2147483648 and max(l) <= 2147483647 else 'long long int')
