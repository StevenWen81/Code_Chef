t = int(input())

for i in range(t):
    l = int(input())
    string = str(input())

    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    ans = "YES"
    for i in dict:
        if dict[i] % 2 != 0:
            ans = "NO"
    
    print(ans)