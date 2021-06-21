l = int(input())
arr = list(map(int, input().split()))

ans = 0
temp = arr[0]
for i in arr[1:]:
    if temp > i:
        ans += temp-i
    else: #temp <= i
        temp = i
        
print(ans)