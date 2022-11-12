t = int(input())

for i in range(t):
    l, cost = map(int, input().split())

    init = 0
    rain = 0
    for i in range(l):
        today = int(input())
        if today == 1:
            rain = 1
            init += cost
        else:
            if rain == 1:
                init += cost
                rain = today
    print(init)


