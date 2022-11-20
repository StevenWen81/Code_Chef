t = int(input())

for i in range(t):
    war = int(input())

    ans = [0 for o in range(10)]
    for j in range(war):
        s = str(input())
        for x in range(10):
            if s[x]=="1" and ans[x]==1:
                ans[x] = 0
            elif s[x]=="1" or ans[x]==1:
                ans[x] = 1
            else:
                ...
    print(sum(ans))