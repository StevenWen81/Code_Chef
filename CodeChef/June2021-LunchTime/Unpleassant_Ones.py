t = int(input())
for i in range(t):
    l = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in arr:
        if i%2==0:
            ans.insert(0,i)
        else:
            ans.append(i)
    print(*ans)