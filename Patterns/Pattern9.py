'''
n = 5
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
'''
n=int(input("Enter number of rows of the pattern that is needed\n"))
spacecount = n-1
for i in range(1,n+1,1):
    print(" "*spacecount,end="")
    print("*"*(2*i-1),end="")
    print(" " * spacecount,end="")
    print()
    spacecount-=1
spacecount = 1
for i in range(n-1,0,-1):
    print(" "*spacecount,end="")
    print("*"*(2*i-1),end="")
    print(" "*spacecount,end="")
    print()
    spacecount+=1
