x = int(input())
total = x * (x+1) / 2

arr = list(map(int, input().split()))
print(int(total - sum(arr)))