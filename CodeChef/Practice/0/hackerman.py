arr = [2, 3, 5, 7, 11]

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    if a+b in arr:
        print("Alice")
    else:
        print("Bob")