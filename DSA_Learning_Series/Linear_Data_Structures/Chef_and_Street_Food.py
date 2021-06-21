tc = int(input())
for i in range(tc):
    t = int(input())
    ans = 0
    for i in range(t):
        a, b ,c = map(int, input().split())
        a += 1
        check = b
        check //= a
        gain = check * c
        ans = max(ans, gain)
    print(ans)