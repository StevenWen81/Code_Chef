t = int(input())
ans = 0
for i in range(t):
    cmd = str(input())
    if cmd == "++X" or cmd == "X++":
        ans += 1
    else:
        ans -= 1
print(ans)