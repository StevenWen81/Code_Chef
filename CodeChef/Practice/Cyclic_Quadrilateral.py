t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    if (arr[0]+arr[2] == 180) and (arr[1]+arr[3] == 180):
        print("YES")
    else:
        print("NO")