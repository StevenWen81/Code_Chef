n = int(input())
check1 = "'"
check2 = "."
check3 = ","
check4 = ";"
check5 = ":"
check6 = "\n"

word = {}
for i in range(n):
    x = list(map(str, input().lower().split()))
    for i in x:
        i = i.replace(check1,"")
        i = i.replace(check2,"")
        i = i.replace(check3,"")
        i = i.replace(check4,"")
        i = i.replace(check5,"")
        i = i.replace(check6,"")
        if i in word:
            word[i] = 1
        else:
            word[i] = 1

ans = []
for i in word:
    ans.append(i)
    
ans.sort()
print(len(ans))
for i in ans:
    print(i)