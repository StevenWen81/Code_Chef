t = int(input())

for i in range(t):
    s,w = map(int, input().split())
    
    bmi = s/(w*w)
    
    if bmi <= 18:
        print("1")
    elif 19<= bmi <= 24:
        print("2")
    elif 25<= bmi <= 29:
        print("3")
    else:
        print("4")