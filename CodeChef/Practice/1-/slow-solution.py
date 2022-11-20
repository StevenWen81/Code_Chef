t = int(input())

for i in range(t):
    maxt, maxn, sumn = map(int, input().split())

    ans = 0
    if sumn//maxn <= maxt:
        ans += maxn**2 * (sumn//maxn)
        if (sumn//maxn) < maxt:
            ans += (sumn%maxn)**2
        else:
            pass
    else:
        ans += maxn**2 * maxt

    print(ans)