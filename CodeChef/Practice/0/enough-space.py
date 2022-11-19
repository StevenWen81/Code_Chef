t = int(input())

for i in range(t):
    room, f1,f2 = map(int, input().split())

    tot = f1 + f2*2

    if room >= tot:
        print("YES")
    else:
        print("NO")