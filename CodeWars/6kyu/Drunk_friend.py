def decode(string_):
    ans = ""
    if type(string_) != str:
        return "Input is not a string"
    else:
        symbl = "abcdefghijklmnopqrstuvwxyz"
        for i in string_:
            helper = symbl.find(i.lower())
            if i.isalpha() and i.islower():
                ans = ans + symbl[::-1][helper]
            elif i.isalpha() and i.isupper():
                ans = ans + symbl[::-1][helper].upper()
            else:
                ans = ans + i
                
    return ans

# print(decode("yvvi"))