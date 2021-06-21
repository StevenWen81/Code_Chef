a = str(input())
a = list(a)
x = []

for i in range(len(a)):
    if a[i].isupper() == True:
        x.append(a[i].lower())
    else:
        x.append(a[i].upper())

for i in x:
    print(i, end = "")
