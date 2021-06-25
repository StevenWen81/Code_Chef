word = str(input())
check = word[0]
word = word[1:]

if check != check.upper():
    check = check.upper()
    
print(check + word)