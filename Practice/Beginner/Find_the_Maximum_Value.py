t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    l = len(arr) - 1
    ind = arr.index(l)
    arr.pop(ind)
    print(max(arr))
    
    