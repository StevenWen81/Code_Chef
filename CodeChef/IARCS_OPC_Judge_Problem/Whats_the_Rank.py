t = int(input())
ans = []
for i in range(1,t+1):
    n = int(input())
    if i == 1:
        print(i)
        ans.append(n)
    elif i == 2:
        ans.append(n)
        if n > ans[0]:
            print(1)
        else:
            print(2)
    else: # i > 2:
        ans.append(n)
        ans.sort(reverse=True)
        x = ans.index(n)
        print(x+1)
    
            