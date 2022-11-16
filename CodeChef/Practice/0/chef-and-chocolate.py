t = int(input())

for i in range(t):
    x, y, z = map(int, input().split())

    coins = 5*x + 10*y

    print(coins//z)