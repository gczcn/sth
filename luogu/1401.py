xl, xu = map(int, input().split())
yl, yu = map(int, input().split())
if \
    -2147483648 <= xl * yl <= 2147483647 and \
    -2147483648 <= xu * yu <= 2147483647 and \
    -2147483648 <= xl * yu <= 2147483647 and \
    -2147483648 <= xu * yl <= 2147483647:
    print('int')
else:
    print('long long int')
