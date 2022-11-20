t = int(input())

for i in range(t):
    l, sw = map(int, input().split())
    pts = [int(x) for x in input().split()]

    motu = []
    tomu = []

    for i in range(l):
        if i%2==0:
            motu.append(pts[i])
        else:
            tomu.append(pts[i])

    for i in range(sw):
        motu.sort()
        tomu.sort()

        if motu[-1] > tomu[0]:
            temp = tomu[0]
            tomu[0] = motu[-1]
            motu[-1] = temp
    
    if sum(tomu) <= sum(motu):
        print("NO") 
    else:
        print("YES")