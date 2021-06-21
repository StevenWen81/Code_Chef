# 100/100
t = int(input())

for i in range(t):
    n = int(input())
    count = 0
    
    while int(n**0.5) >= 1:
        x = int(n**0.5)
        n -= x**2
        count += 1
    
    print(count)
    