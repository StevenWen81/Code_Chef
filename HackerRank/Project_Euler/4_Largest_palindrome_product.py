def solve():
    pmax = input()
    tmp = 0
    for i in range(110, 1000, 11):
        for j in range(100, 1000):
            p = i*j
            if int(p) < int(pmax) and str(p) == str(p)[::-1] and int(p) > int(tmp):
                tmp = p
    print (tmp)    

t = int(input())
for i in range(t):
    solve()