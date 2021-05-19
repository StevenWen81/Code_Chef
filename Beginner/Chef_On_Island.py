t = int(input())

for i in range(t):
    a,b,aa,bb,d = map(int, input().split())
    a -= aa * d
    b -= bb * d
    
    if a >= 0 and b >= 0:
        print("YES")
    else:
        print("NO")
 
    