t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    ans = 1
    
    while a//b != 0:
        a = a//b
        ans += 1
    
    print(ans)