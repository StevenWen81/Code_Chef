word = str(input())

count_l = 0
count_u = 0

for i in word:
    if i.isupper() == True:
        count_u += 1
    else:
        count_l += 1
        
if count_l >= count_u:
    print(word.lower())
else:
    print(word.upper())