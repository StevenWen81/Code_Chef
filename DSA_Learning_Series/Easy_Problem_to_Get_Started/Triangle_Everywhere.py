arr = list(map(int, input().split()))
arr.sort()

while True:
    if arr[0]+arr[1]>arr[2] and arr[1]+arr[2]>arr[0] and arr[0]+arr[2]>arr[1]:
        if arr[0] == arr[1] and arr[1] == arr[2]:
            print(1)
            break
        if arr[0] == arr[1] and arr[1] != arr[2]:
            print(2)
            break
        print(3)
        break
    else:
        print(-1)
        break