t = int(input())

for i in range(t):
    init, want, hot, cool = map(int, input().split())

    gap = init - want

    ans = "NO"
    if gap > 0:
        if cool>=gap:
            ans = "YES"
    if gap < 0:
        if hot >= abs(gap):
            ans = "YES"
    if gap == 0:
        ans = "YES"
    
    print(ans)