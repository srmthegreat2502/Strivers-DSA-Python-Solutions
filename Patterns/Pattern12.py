'''
n = 4
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
'''
n = int(input("Enter the number of rows of the pattern that is needed\n"))
space = 2*n-2
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print(" "*(space*2),end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    space-=2
