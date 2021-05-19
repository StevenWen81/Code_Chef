# 100/100
t = int(input())

for i in range(t):
    s,w,c = map(int, input().split())
    
    ans = w + (100-s)*c
    
    print(ans*10)