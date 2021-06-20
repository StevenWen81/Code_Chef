n = int(input())
blank = n-1
count = 0
while count != n:
    print(blank*" ",end = "")
    print((n-blank)*"*", end = "")
    print()
    count += 1
    blank -= 1