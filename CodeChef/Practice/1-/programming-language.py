t = int(input())

for i in range(t):
    a,b, a1,b1, a2,b2 = map(int, input().split())

    one = [a1, b1]
    two = [a2, b2]

    ans = 0
    if a in one and b in one:
        ans = 1
    if a in two and b in two:
        ans = 2
    
    print(ans)