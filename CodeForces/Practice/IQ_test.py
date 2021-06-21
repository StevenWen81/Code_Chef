l = int(input())
arr = list(map(int, input().split()))
even = []
odd = []
for i in arr:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
if len(even) == 1:
    ans = arr.index(even[0])

if len(odd) == 1:
    ans = arr.index(odd[0])
    
print(ans + 1)