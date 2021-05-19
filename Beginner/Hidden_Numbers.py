t = int(input())

for i in range(t):
    x = int(input())
    
    if x%2==0:
        ans_helper = x//2
        print("2", ans_helper)
    else:          
        print("1", x)