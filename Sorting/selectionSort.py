print("Enter the list as comma separated integers")
l = list(map(int,input().split(",")))
print("list is ", l)
for i in range(0,len(l)-1):
    small = l[i]
    smalli = i
    for j in range(i+1, len(l)):
        if l[j]<small:
            small=l[j]
            smalli=j
    l[i], l[smalli] = l[smalli], l[i]
    print("After an iteration", l)



