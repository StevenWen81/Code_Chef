n = int(input())
ans = [0,1,2]
if n==1:
    print(ans[n])
if n==2:
    print(ans[n])
if n > 2:
    s = 1
    w = 2
    temp = 0
    for i in range(3, n+1):
        temp = (s+w) % 15746
        ans.append(temp)
        s = w % 15746
        w = temp
    print(ans[-1])
    