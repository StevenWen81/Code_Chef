t = int(input())
arr = []
for i in range(t):
    c, p, d = map(int, input().split())
    head = c
    rest = p + d
    arr.append([head, rest])

# sort by the index 1 value 
arr.sort(key = lambda x:x[1], reverse = True)
#print(arr)
add = 0
ans =  0
for i in arr:
    add += i[0]
    check = add + i[1]
    ans = max(ans, check)
print(ans)
