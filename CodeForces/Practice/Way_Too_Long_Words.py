t = int(input())

for i in range(t):
    word = str(input())
    l = len(word)
    if l > 10:
        print(word[0] + str(l-2) + word[l-1])
    else:
        print(word)