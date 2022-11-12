t = int(input())

for i in range(t):
    h, x, y = map(int, input().split())
    if x > y:
        print(1)
    else:
        print(0)