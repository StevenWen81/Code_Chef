t = int(input())

for i in range(t):
    l, money = map(int, input().split())

    p = [int(x) for x in input().split()]

    check = [0 for o in range(l)]

    for i in range(l):
        if money >= p[i]:
            check[i] = max(check[i], 1)
            money -= p[i]
    
    ans =""
    for i in check:
        ans += str(i)
    print(ans)