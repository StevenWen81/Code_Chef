t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    second = []
    temp = arr.copy()
    temp.sort()
    pt = 0
    for i, j in enumerate(arr):
        if j != temp[pt]:
            second.append(j)
        else:
            pt += 1
    temp2 = second.copy()
    temp2.sort()
    if temp2 == second:
        print("YES")
    else:
        print("NO")