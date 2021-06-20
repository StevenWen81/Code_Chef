# 100/100
t = int(input())

for i in range(t):
    x = input()
    count = 0
    
    for i in x:
        if i == '4':
            count += 1
        
    print(count)