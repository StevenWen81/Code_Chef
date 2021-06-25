t = int(input())
helper = {}
arr = []
for i in range(t):
    x = int(input())
    arr.append(x)
    if x in helper:
        helper[x] += 1
    else:
        helper[x] = 1
#print(helper)

ans = 0    
used = []
#debug = []
for i in range(t):
    for j in range(i):
        check = (arr[i] + arr[j])
        if check%2 == 0:
            check = check//2
            #debug.append(check)
            if (check in helper) and (check not in used):
                #print(check)
                #print(helper[check])
                ans += helper[check]
                used.append(check)
#print(used)
#print(debug)
print(ans)