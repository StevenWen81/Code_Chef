def solve(x,y):
    helper = {}
    for i in x:
        if i in helper:
            helper[i] += 1
        else:
            helper[i] = 1
    for j in y:
        if j in helper:
            helper[j] -= 1
        else:
            helper[j] = 1
    for i in helper:
        if helper[i] != 0:
            return "NO"
    return "YES"

t = int(input())
for i in range(t):
    word =  str(input())
    length = len(word)
    
    if length%2 == 0:
        left = word[0:length//2]
        right = word[length//2:length]
        print(solve(left, right))
        #print(left)
        #print(right)
        
    else:
        left = word[0:length//2]
        right = word[length//2+1:length]
        print(solve(left, right))
        #print(left)
        #print(right)