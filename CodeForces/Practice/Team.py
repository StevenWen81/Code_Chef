t = int(input())
ans = 0
for i in range(t):
    arr = list(map(int, input().split()))
    sure = arr.count(1)
    if sure >= 2:
        ans += 1
print(ans)