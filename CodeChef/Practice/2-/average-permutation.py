t = int(input())

for i in range(t):
    x = int(input())

    if x==3:
        print(3,2,1)
    else:
        ans = []

        ans.append(x-1)
        ans.append(x-2)

        if x>4:
            for i in range(1, x-3):
                ans.append(i)
        
        ans.append(x-3)
        ans.append(x)

        print(*ans)