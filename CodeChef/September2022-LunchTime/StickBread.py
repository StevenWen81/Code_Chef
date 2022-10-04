t = int(input())

for i in range(t):
    stick_len, quant= map(int, input().split())
    
    if (stick_len%quant == 0):
        print(0)
    else:
        print(1)