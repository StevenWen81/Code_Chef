# 100/100
t = int(input())

for i in range(t):
    s,w = map(int, input().split())
    
    if s < w:
        print("<")
    if s > w:
        print(">")
    if s == w:
        print("=")