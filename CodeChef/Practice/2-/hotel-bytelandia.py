t = int(input())

for i in range(t):
    n = int(input())
    ins = [int(x) for x in input().split()]
    out = [int(y) for y in input().split()]

    dict = {}

    for i in range(n):
        for j in range(ins[i], out[i]):
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1
    
    print(max(dict.values()))