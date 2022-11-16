t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    zero = 0
    one = 0
    
    for i in arr:
        if i == 0:
            zero += 1
        if i == 1:
            one += 1
            
    if  zero>0 and one>0:
        print(1)
    else:
        print(0)