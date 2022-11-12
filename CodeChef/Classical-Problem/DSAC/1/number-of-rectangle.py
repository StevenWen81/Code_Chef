# count all rectangle on n*m grid
def rect(n,m):
    for_n = n*(n+1)//2
    for_m = m*(m+1)//2
    return (for_n*for_m)

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    ans = rect(n,m) - n*m
    print(ans)