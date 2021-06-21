t = int(input())
for i in range(t):
    car = int(input())
    speed = list(map(int, input().split()))
    ans = 1
    temp = speed[0]
    
    if car == 1:
        print(ans)
    else: # car > 1
        for i in range(1, car):
            #print(speed[i])
            if temp >= speed[i]:
                ans += 1
                temp = speed[i]
        print(ans)