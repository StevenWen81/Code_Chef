t = int(input())
for i in range(t):
    x = str(input())
    front = x[0]
    back = x[len(x)-1]
    ans = int(front) + int(back)
    print(ans)