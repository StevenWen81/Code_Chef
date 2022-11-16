t = int(input())

for i in range(t):
    x, y, a = map(int, input().split())

    if x<=a<y:
        print("YES")
    else:
        print("NO")