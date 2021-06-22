t = int(input())

for i in range(t):
    ans = 0
    n = int(input())
    ans += pow(n,2) * pow(n+1,2) / 4
    ans -= n * (n + 1) * (2*n + 1) / 6
    print(int(ans))