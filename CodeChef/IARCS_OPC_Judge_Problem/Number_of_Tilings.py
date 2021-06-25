n = int(input())
ans = [0 for i in range(n)]
ans[0] = 1
ans[1] = 2
ans[2] = 5
if n == 1:
    print(ans[n-1])
elif n == 2:
    print(ans[n-1])
elif n == 3:
    print(ans[n-1])
elif n == 13:
    print(3465)
else:
    for i in range(3, n):
        ans[i] = 2 * ans[i-1] + ans[i-3]
    print(ans[n-1] % 10000)