n = int(input())
ans = []
arr = []
for i in range(1, (n*5)+1):
    arr.append(i)

for slicing in range(n):
    ans.append(arr[slicing*5:(slicing+1)*5])

for i in range(n):
    if i%2==0:
        ans[i] = ans[i]
    else:
        ans[i] = ans[i][::-1]

for i in ans:
    print(*i)
        