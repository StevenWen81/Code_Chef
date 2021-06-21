n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dif = [0]*(n-1)

for i in range(n-1):
    dif[i] = abs(arr[i] - arr[i+1])
    
flag = max(dif)
ans = float(flag / 2)
ans_front = 0
ans_back = 0

if 0 not in arr:
    ans_front = arr[0]
if l not in arr:
    ans_back = arr[l-1]

print(max(ans, ans_front, ans_back))