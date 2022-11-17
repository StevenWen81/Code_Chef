t = int(input())

for i in range(t):
    l = int(input())
    arr = [int(x) for x in input().split()]

    ans = sum(arr)**2 - sum(arr)
    ans %= 998244353
    print(ans)