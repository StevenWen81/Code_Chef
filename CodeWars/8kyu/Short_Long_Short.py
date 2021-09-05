def solution(a, b):
    la = len(a)
    lb = len(b)
    ans = ""
    
    if la < lb:
        ans = a + b + a
    else:
        ans = b + a + b
        
    return ans

# print(solution('45', '1'))