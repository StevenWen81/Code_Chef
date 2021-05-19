t = int(input())

for i in range(t):
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        p = map(int, input().split())
        ans = ans ^ i
    print(ans)