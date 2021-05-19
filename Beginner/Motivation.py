# 100/100
t = int(input())

for i in range(t):
    arr = []
    n,x = map(int, input().split())
    
    for i in range(n):
        si, ri = map(int, input().split())
        
        if si <= x:
            arr.append(ri)
    
    print(max(arr))