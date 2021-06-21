s,e = map(int, input().split())
ans = []
for i in range(s, e+1):
    if i % 2 != 0:
        ans.append(i)
print(*ans)