t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    arr = [int(x) for x in input().split()]

    ans = "NO"
    if n==1:
        if arr[0] == k:
            ans = "YES"
    else:
        for i in range(n-1):
            if arr[i] == k:
                ans = "YES"
    
    print(ans)