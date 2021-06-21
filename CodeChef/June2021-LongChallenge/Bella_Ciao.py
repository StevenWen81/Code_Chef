# 100/100
t = int(input())
for i in range(t):
    ans = 0
    D,d,P,Q = map(int,input().split())
    ans += P*D
    x = (D-1) % d
    y = (D-1)//d - 1
    ans += d*Q*y*(y+1)//2+(y+1)*Q*(x+1)    
    print(ans)
    