# 100/100
t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    arr = list(map(int, input().split()))
    
    sum_arr = 0
    for i in arr:
        sum_arr += i      
    
    if sum_arr%b == 0:
        print("0")
    else:
        print("1")