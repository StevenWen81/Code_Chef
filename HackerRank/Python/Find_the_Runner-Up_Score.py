def solve(arr):
    biggest = arr[0]
    for i in arr[1:]:
        if i != biggest:
            return i

l = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
#print(arr)
print(solve(arr))