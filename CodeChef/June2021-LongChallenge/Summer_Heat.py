# 100/100
t = int(input())
for i in range(t):
    ans = 0
    a,b,ac,bc = map(int,input().split())
    ans += ac//a
    ans += bc//b
    print(ans)
    