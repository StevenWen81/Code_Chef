def solve():
    n = int(input())
    while n % 2 == 0:
        n //= 2
    d = 3
    while d*d <= n:
        if(n % d== 0):
            n //= d
        else:
            d += 2
    print(n)    

t = int(input())

for i in range(t):
    solve()
