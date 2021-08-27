def rankdiv(x):
    if x < 1600:
        print(3)
    if 1600<= x < 2000:
        print(2)
    if 2000 <= x:
        print(1)

t = int(input())
for i in range(t):
    x = int(input())
    rankdiv(x)
