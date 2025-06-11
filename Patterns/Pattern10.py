'''
n=3
*
**
***
**
*
'''
n = int(input("Enter the number of rows of the pattern that is needed\n"))
for i in range(0,n,1):
    for j in range(0,i+1):
        print("*",end="")
    print()
for i in range(n-1,-1,-1):
    for j in range(0,i+1):
        print("*",end="")
    print()
