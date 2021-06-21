# 100/100
# Note: Only 1 win for each O and/or X
def requirement(word, ch):
    # check for 0 1 2
    if (word[0]==ch) and (word[0]==word[1]) and (word[0]==word[2]):
        return 1
    # check for 3 4 5
    elif (word[3]==ch) and (word[3]==word[4]) and (word[3]==word[5]):
        return 1
    # check for 6 7 8
    elif (word[6]==ch) and (word[6]==word[7]) and (word[6]==word[8]):
        return 1
    # check for 0 3 6
    elif (word[0]==ch) and (word[0]==word[3]) and (word[0]==word[6]):
        return 1
    # check for 1 4 7
    elif (word[1]==ch) and (word[1]==word[4]) and (word[1]==word[7]):
        return 1
    # check for 2 5 8
    elif (word[2]==ch) and (word[2]==word[5]) and (word[2]==word[8]):
        return 1
    # check for 0 4 8
    elif (word[0]==ch) and (word[0]==word[4]) and (word[0]==word[8]):
        return 1
    # check for 2 4 6
    elif (word[2]==ch) and (word[2]==word[4]) and (word[2]==word[6]):
        return 1
    else:
        return 0

t = int(input())

for i in range(t):
    a = str(input())
    b = str(input())
    c = str(input())
    word = a+b+c
    x_win = requirement(word,"X")
    o_win = requirement(word,"O")
    x_count = 0
    o_count = 0
    blank_count = 0
    
    for i in word:
        if i == "X":
            x_count += 1
        if i == "O":
            o_count += 1
        
    blank_count = 9 - x_count - o_count
    
    #print(x_count)
    #print(o_count)
    #print(blank_count)
    while True:
        if x_count < o_count:
            print(3)
            #print('a')
            break
        if x_count > o_count+1:
            print(3)
            #print('b')
            break
        
        if (x_win==1) and (o_win==1):
            print(3)
            #print('c')
            break
        elif (x_win==1) and (x_count==o_count):
            print(3)
            #print('d')
            break
        elif (o_win==1) and (x_count>o_count):
            print(3)
            #print('e')
            break
        elif (o_win==1) or (x_win==1):
            print(1)
            #print('f')
            break
        elif (blank_count==0):
            print(1)
            #print('g')
            break
        else:
            print(2)
            #print('h')
            break
    
