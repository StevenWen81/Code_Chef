a, b, c = map(int, input().split())

helper = {}
ans = []

for i in range(a+b+c):
    x = int(input())
    if x in helper:
        helper[x] += 1
    else:
        helper[x] = 1
        
for i in helper:
    if helper[i] >= 2:
        ans.append(i)
        
ans.sort()
print(len(ans))
for i in ans:
    print(i)