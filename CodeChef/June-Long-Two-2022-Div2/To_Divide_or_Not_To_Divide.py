t = int(input())

for i in range(t):
    a, b, n = map(int, input().split())
    res = n%a
    init = n//a
    
    if res > 0:
        init += 1
    ans = a * init
    
    if a%b == 0:
        print(-1)
    else:
        if ans % b == 0:
            print(ans + a)
        else:
            print(ans)