t = int(input())

for i in range(t):
    x, p = map(int, input().split())

    # number power p mod 10
    temp = str(x)
    l = len(temp)

    new = ""
    num = 0
    for i in range(l):
        num = x // (10**(l-1-i))
        num **= p
        new += str(num%10)
        x %= 10**(l-1-i)
    
    # print(new)
    ans = ""
    for i in new:
        ans = i + ans
    
    if int(ans)%7 == 0:
        print("YES")
    else:
        print("NO")
    