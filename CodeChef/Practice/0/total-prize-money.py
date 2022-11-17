t = int(input())

for i in range(t):
    ten, rest = map(int, input().split())

    prize = 10*ten + 90*rest
    print(prize)