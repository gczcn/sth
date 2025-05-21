L, R = input().split()
L = int(L)
R = int(R)
c = 0

for i in range(0, len(str(R))):  # 遍历每一位
    power = 10 ** i
    next_power = 10 ** (i + 1)
    
    # 计算当前位为2时的贡献
    higher = (R // next_power) - (L // next_power)
    c += higher * power
    
    # 处理当前位刚好是2的情况
    current_R = (R // power) % 10
    current_L = (L // power) % 10
    
    if current_R > 2:
        c += power
    elif current_R == 2:
        c += (R % power) + 1
    
    if current_L > 2:
        c -= power
    elif current_L == 2:
        c -= (L % power)
    
print(c)
