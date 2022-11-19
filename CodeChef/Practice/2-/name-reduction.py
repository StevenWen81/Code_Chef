t = int(input())

for i in range(t):
    a, b = map(str, input().split())

    n = int(input())
    c = ""
    for j in range(n):
        temp = str(input())
        c += temp
    
    parent = a+b

    dict = {}
    for i in parent:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    # print(dict)

    for i in c:
        if i in dict:
            dict[i] -= 1
        else:
            dict[i] = -1
    
    # print(dict)
    ans = "YES"
    for i in dict:
        if dict[i] < 0:
            ans = "NO"

    print(ans)