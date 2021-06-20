t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    helper = 0
    ans = 0
    
    for i in arr:
        helper = helper + i - k
        if helper >= 0:
            ans += 1
        else:
            break
        
    if helper >= 0:
        ans += helper // k
    
    print(ans + 1)