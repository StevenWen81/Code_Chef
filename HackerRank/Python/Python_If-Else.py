n = int(input())
if n%2!=0:
    print("Weird")
else:
    arr1 = []
    for i in range(2,6):
        arr1.append(i)
    
    arr2 = []
    for i in range(6,21):
        arr2.append(i)
    
    if n in arr1:
        print("Not Weird")
    
    if n in arr2:
        print("Weird")
    
    if n > 20:
        print("Not Weird")