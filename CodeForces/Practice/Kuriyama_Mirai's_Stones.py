l = int(input())
arr = list(map(int,input().split()))
s_arr = arr.copy()
s_arr.sort()

t = int(input())
for i in range(t):
    choice,  s, e = map(int, input().split())
    if choice == 1:
        print(sum(arr[s-1:e]))
    if choice == 2:
        print(sum(s_arr[s-1:e]))
    