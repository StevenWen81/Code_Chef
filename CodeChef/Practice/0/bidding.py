def solve(who, arr):
    for i in range(len(arr)):
        if arr[i] == max(arr):
            return who[i]


t = int(input())

for i in range(t):
    who = ["Alice", "Bob", "Charlie"]

    arr = [int(x) for x in input().split()]

    print(solve(who, arr))

