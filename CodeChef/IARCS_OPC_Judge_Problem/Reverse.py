n = int(input())
ans = [] 
check1 = "'"
check2 = "."
check3 = ","
check4 = ";"
check5 = ":"
for i in range(n):
    line = list(map(str, input().split()))
    temp = []
    for i in line:
        i = i.replace(check1,"")
        i = i.replace(check2,"")
        i = i.replace(check3,"")
        i = i.replace(check4,"")
        i = i.replace(check5,"")
        temp.append(i)
    ans.append(temp)

ans = ans[::-1]
for i in ans:
    i = i[::-1]
    print(*i)