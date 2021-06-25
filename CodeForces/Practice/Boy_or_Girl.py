name = str(input())
helper = {}

for i in name:
    if i in helper:
        helper[i] += 1
    else:
        helper[i] = 1
check = len(helper)
if check%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")