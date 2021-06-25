t = int(input())
# [total_points, max_lead]
one_arr = [0,0]
two_arr = [0,0]

for i in range(t):
    player1, player2 = map(int, input().split())
    one_arr[0] += player1
    two_arr[0] += player2
    
    if one_arr[0] > two_arr[0]:
        if (one_arr[0]-two_arr[0]) > one_arr[1]:
            one_arr[1] = one_arr[0]-two_arr[0]
        else:
            one_arr[1] = one_arr[1] # nothing change
    else: # two_arr[0] > one_arr[0]:
        if (two_arr[0]-one_arr[0]) > two_arr[1]:
            two_arr[1] = two_arr[0]-one_arr[0]

if one_arr[1] > two_arr[1]:
    print("1", one_arr[1])
else:
    print("2", two_arr[1])