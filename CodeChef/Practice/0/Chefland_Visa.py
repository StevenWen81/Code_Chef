t = int(input())

for i in range(t):
    a,b, c,d, e,f = map(int, input().split())
    
    if b>=a and d>=c and f<=e:
        print("YES")
    else:
        print("NO")