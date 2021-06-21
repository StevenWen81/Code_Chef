t = int(input())
helper = []
for i in range(t):
    name, mark1, mark2, mark3 = map(str, input().split())
    helper.append([name, mark1, mark2, mark3])

ans = 0    
stu = str(input())
#print(helper)
for i in helper:
    if i[0] == stu:
        ans += float(i[1])
        ans += float(i[2])
        ans += float(i[3])
        ans /= 3
print("%.2f" % ans)