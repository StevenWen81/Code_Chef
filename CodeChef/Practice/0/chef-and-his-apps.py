t = int(input())

for i in range(t):
    s, x, y, z = map(int, input().split())

    if x>=y:
        big = x
    else:
        big = y

    space = s - x - y

    unin = 0

    if space >= z:
        pass
    elif space + big >= z:
        unin += 1
    else:
        unin += 2
    
    print(unin)