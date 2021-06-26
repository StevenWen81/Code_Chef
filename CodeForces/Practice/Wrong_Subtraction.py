num, time = map(int, input().split())

for i in range(time):
    if num%10 == 0:
        num //= 10
    else:
        num -= 1
        
print(num)