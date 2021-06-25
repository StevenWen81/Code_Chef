def helper(words):
    maxLength = 1
    start = 0
    length = len(words)
    begin = 0
    end = 0
    for i in range(1, length):
        begin = i - 1
        end = i
        while begin >= 0 and end < length and words[begin] == words[end]:
            check = end - begin + 1
            if check > maxLength:
                start = begin
                maxLength = check
            begin -= 1
            end += 1
        begin = i - 1
        end = i + 1
        while begin >= 0 and end < length and words[begin] == words[end]:
            check = end - begin + 1
            if check > maxLength:
                start = begin
                maxLength = check
            begin -= 1
            end += 1
    return(words[start:start+maxLength])
            
t = int(input())
stri = str(input())
long = helper(stri)
length = len(long)

ans = []
ans.append(length)
ans.append(long)

for i in ans:
    print(i)