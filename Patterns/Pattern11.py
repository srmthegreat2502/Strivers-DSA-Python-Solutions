'''
n=4
1
0 1
1 0 1
0 1 0 1
'''
n = int(input("Enter the number of rows of the pattern that is needed\n"))
for i in range(1,n+1):
    if(i%2==0):
        start = 0
        next = 1
    else:
        start = 1
        next = 0
    for j in range(1,i+1):
        if(j%2==1):
            print(start, end=" ")
        else:
            print(next, end=" ")
    print()