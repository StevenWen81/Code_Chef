n = int(input())
arr = list(map(int, input().split()))

ans = []
final = []

for i in range(1, n+1):
    ans.append(i)
    
while len(ans) != 0:
    i = ans[0]
    mark = ans[0]
    capt = [i]
    ans.remove(ans[0])
    while mark != arr[i-1]:
        capt.append(arr[i-1])
        ans.remove(arr[i-1])
        i = arr[i-1]
    capt.append(mark)
    final.append(capt)
    
print(len(final))
for i in final:
    for j in i:
        print(j,end=" ")
    print()