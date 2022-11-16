t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    check = a+b
    
    if check < 3:
        print(1)
    
    if 3 <= check <= 10:
        print(2)
    
    if 11 <= check <= 60:
        print(3)
    
    if 60 < check:
        print(4)