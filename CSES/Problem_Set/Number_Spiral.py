def solve():
    y,x = map(int, input().split())
    if max(y,x) == x:
        if x%2==1:
            print(pow(x,2)-y+1)
        else:
            x -= 1
            print(pow(x,2) + y)
    else:
        if y%2==0:
            print(pow(y,2)-x+1)
        else:
            y -= 1
            print(pow(y,2) + x)

t = int(input())
for i in range(t):
    solve()