t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    ans = 0
    ct = 0
    for i in arr:
        if i == 1:
            ct += 1
        else:
            ans += (ct)*(ct+1)//2 
            ct = 0
    if ct > 0:
        ans += (ct)*(ct+1)//2 
    print(ans)