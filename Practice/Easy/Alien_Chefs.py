n = int(input())
hold = []
for i in range(n):
    apply = list(map(int, input().split()))
    hold.append(apply)
    
t = int(input())
for i  in range(t):
    ans = 0
    helper = []
    check = list(map(int, input().split()))
    for i in range(1, len(check)):
        for j in hold:
            if (j[0]<=check[i]<=j[1]) and (j[0] not in helper):
                helper.append(j[0])
                ans += 1
    print(ans)