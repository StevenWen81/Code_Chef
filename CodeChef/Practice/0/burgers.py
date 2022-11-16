t = int(input())

for i in range(t):
    bun, meat = map(int, input().split())

    if bun <= meat:
        print(bun)
    else:
        print(meat)