t = int(input())

for i in range(t):
    n = int(input())
    if n%2==0:
        begin = 2
    else:
        begin = 1
    ans = 0
    
    for i in range(begin, n+1, 2):
        ans += i*i
    print(ans)
