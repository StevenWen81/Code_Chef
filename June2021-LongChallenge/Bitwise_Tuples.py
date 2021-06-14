# 100/100
def pangkat(a,b):
    if b == 0:
        return 1
    x = pangkat(a,b//2) % 1000000007
    x *= x
    if b%2 == 1:
        x *= a
    return x

t = int(input())
for i in range(t):
    ans = 0
    n,m = map(int, input().split())
    ans = pangkat(2,n)
    ans -= 1
    ans = pangkat(ans,m)
    ans = ans % 1000000007
    print(ans)