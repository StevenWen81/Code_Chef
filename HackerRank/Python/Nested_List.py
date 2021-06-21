t = int(input())
arr = []
for i in range(t):
    name = str(input())
    score = float(input())
    arr.append([name,score])
arr.sort(key=lambda x:x[1])
#print(arr)

ans = []
#check for second smallest
smallest = arr[0][1]
for i in arr:
    if i[1] != smallest:
        second = i[1]
        break
    
for i in arr:
    if i[1] == second:
        ans.append(i[0])
        
ans.sort()
for i in ans:
    print(i)