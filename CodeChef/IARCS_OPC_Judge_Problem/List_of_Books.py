m = int(input())
library = list(map(int, input().split()))
ans = []

t = int(input())
for i in range(t):
    ind = int(input())
    ans.append(library[ind-1])
    library.pop(ind-1)
    
for i in ans:
    print(i)