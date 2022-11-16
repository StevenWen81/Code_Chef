t = int(input())

for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())

    one = x1+y1
    two = x2+y2

    print(min(one,two))