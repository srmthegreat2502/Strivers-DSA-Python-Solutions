print("Enter the list as comma separated values")
l = list(map(int,input().split(",")))
for i in range(len(l)-1, -1, -1):
    for j in range(0,i):
        if(l[j]>l[j+1]):
            l[j], l[j+1] = l[j+1], l[j]
    print("After an iteration ", l)
