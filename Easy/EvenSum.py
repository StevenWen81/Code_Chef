# 100/100
t = int(input())

for i in range(t):
    length_arr = int(input())
    arr = list(map(int, input().split()))
    add = 0
    
    for i in arr:
        add += i
        
    if add%2 == 1:
        print(2)
    else:
        print(1)