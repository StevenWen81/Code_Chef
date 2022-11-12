t = int(input())

for i in range(t):
    p, x, y, z = map(int, input().split())
    
    ep = p
    if z == 1:
        ep += y/100*p
    else:
        ep -= x/100*p

    print(ep)