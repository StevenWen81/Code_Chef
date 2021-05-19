t = int(input())

for i in range(t):
    n = int(input())
    ans = 0
    if n<4:
        print(ans)
    else:
        n = int(n/2)
        ans = int(n*(n-1)/2)
        print(ans)