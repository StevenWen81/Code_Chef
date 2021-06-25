word1 = str(input())
word2 = str(input())
word1 = word1.lower()
word2 = word2.lower()

if word1==word2:
    print(0)
else:
    arr = [word1,word2]
    arr.sort()
    if arr[0] == word1:
        print(-1)
    else:
        print(1)