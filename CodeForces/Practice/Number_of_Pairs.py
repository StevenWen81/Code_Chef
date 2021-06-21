t = int(input())

for i in range(t):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        for j in range(i):
            if l <= (arr[i]+arr[j]) <= r:
                ans += 1
                
    print(ans)