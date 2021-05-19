s = int(input())
arr = [100, 50, 0]

if 1 <= s <= 50:
    print(arr[0])
elif 51 <= s <= 100:
    print(arr[1])
else:
    print(arr[2])