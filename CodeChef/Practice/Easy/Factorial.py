t = int(input())
for i in range(t):
    x = int(input())
    flag = 5
    ans = 0
    multi = 1
    while flag <= x:
        ans += x//(pow(5,multi))
        multi += 1
        flag = pow(5,multi)
    print(ans)