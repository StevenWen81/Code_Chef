a, b, c = map(int, input().split())

arr = []

arr.append(a-b)
arr.append(a-b-c)

print(*arr)