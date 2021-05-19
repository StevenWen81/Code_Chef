s,w,c = map(int, input().split())

left_chances = 20 - w

max_points = 36 * left_chances

if s < (c+max_points):
    print("YES")
else:
    print("NO")