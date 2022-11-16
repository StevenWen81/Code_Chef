t = int(input())

for i in range(t):
    w, x, y, z = map(int, input().split())

    arr = []
    arr.append(x)
    arr.append(y)
    arr.append(z)

    if w in arr:
        print("YES")
    elif w == x+y or w == y+z or w == z+x:
        print("YES")
    elif w == x+y+z:
        print("YES")
    else:
        print("NO")