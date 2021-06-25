t = int(input())
arr = []
for i in range(t):
    x = int(input())
    arr.append(x)

mark = [1]*t
#print(mark)
for i in range(t):
    for j in range(i):
        #print(arr[j], arr[i])
        if arr[i] % arr[j] == 0:
            mark[i] = max(mark[i], mark[j]+1)
            
#print(mark)            
print(max(mark))