t = int(input())

for i in range(t):
    n, m, cost = map(int, input().split())

    print(2*(n+m)*cost)