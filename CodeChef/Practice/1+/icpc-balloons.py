solve = [1, 2, 3, 4, 5, 6, 7]

t = int(input())

for i in range(t):
    l = int(input())
    prob = [int(x) for x in input().split()]

    req = 0
    count = 0
    for i in range(l):
        if prob[i] in solve:
            count += 1
            req += 1
            if req==7:
                break
        else:
            count += 1
    
    print(count)
