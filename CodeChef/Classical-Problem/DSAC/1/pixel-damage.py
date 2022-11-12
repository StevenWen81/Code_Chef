t = int(input())

for i in range(t):
    h, w, x, y, k = map(int, input().split())

    x_ax = (w-x)**2
    y_ax = (h-y)**2

    ans = (x_ax + y_ax)**0.5
    
    if ans < k:
        print(1)
    else:
        print(0)