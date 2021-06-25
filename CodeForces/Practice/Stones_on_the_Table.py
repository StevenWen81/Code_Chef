t = int(input())
stone = str(input())
ans = 0

for i in range(t-1):
    if stone[i] == stone[i+1]:
        ans += 1
print(ans)