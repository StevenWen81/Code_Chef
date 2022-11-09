def gcd(x, y):

    while(y):
        x, y = y, x % y

    return x

t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    sol = False
    st = gcd(a,b)
    if b == 1:
        sol = True
    while gcd(a,b) > 1:
        b //= st
        if b == 1:
            sol = True
            break
        st = gcd(a,b)
    if sol:
        print("YES")
    else:
        print("NO")