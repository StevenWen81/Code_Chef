t = int(input())

for i in range(t):
    cho, can = map(int, input().split())

    cho *= 2
    can *= 5

    if cho > can:
        print("Chocolate")
    if cho == can:
        print("Either")
    if cho < can:
        print("Candy")