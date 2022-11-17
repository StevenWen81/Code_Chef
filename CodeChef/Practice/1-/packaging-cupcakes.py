import math

t = int(input())

for i in range(t):
    x = int(input())

    spare = x/2 + 1
    spare = math.floor(spare)

    print(spare)