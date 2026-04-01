print("Enter the list as comma separated values")
l = list(map(int,input().split(",")))
for i in range(0,len(l)):
    j=i
    while(j>0 and l[j]<l[j-1]):
        l[j], l[j-1] = l[j-1], l[j]
        j-=1
    print("After an iteration ",l)