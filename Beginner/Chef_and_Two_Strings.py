t = int(input())

for i in range(t):
    s1 = str(input())
    s2 = str(input())
    
    best = 0
    worst = 0
        
    for i in range(len(s1)):
        # best case
        if s1[i] != "?" and s2[i] == "?":
            best += 0
        if s1[i] == "?" and s2[i] != "?":
            best += 0
        if s1[i] == "?" and s2[i] == "?":
            best += 0
        if (s1[i] != s2[i]) and s1[i] != "?" and s2[i] != "?":
            best += 1
        
        # worst case
        if s1[i] != "?" and s2[i] == "?":
            worst += 1
        if s1[i] == "?" and s2[i] != "?":
            worst += 1
        if s1[i] == "?" and s2[i] == "?":
            worst += 1    
        if (s1[i] != s2[i]) and s1[i] != "?" and s2[i] != "?":
            worst += 1        
    
    print(best, worst)