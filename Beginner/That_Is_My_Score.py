# 100/100
t = int(input())

for i in range(t):
    q = int(input())
    arr = [0]*11
    ans = 0
    for i in range(q):
        s,w = map(int, input().split())
        if arr[s-1] < w:
            arr[s-1] = w
    
    for i in range(9-1):
        ans += arr[i]
        
    print(ans)