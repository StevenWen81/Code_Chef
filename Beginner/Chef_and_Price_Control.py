t = int(input())

for i in range(t):
    s,w = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_one = sum(arr)

    
    for i in range(s):
        if arr[i] > w:
            arr[i] = w

    sum_two = sum(arr)
    
    print(sum_one - sum_two)