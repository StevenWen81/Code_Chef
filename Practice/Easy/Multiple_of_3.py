t = int(input())

for i in range(t):
    length, one, two = map(int, input().split())
    l = length - 2
    num = one + two
    if l > 0:
        if (num%10)%5 == 0:
            num = num + (num%10)
        else:
            num = num + (num%10) + int((l-1)/4) * 20
            check = (one + two) % 10
            for i in range((l-1) % 4):
                check = 2*check
                check %= 10
                num += check
    if num % 3 == 0:
        print("YES")
    else:
        print("NO")