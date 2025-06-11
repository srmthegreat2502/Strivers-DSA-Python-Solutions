'''
n=5
*********
 *******
  *****
   ***
    *
'''
n = int(input("Enter the number of rows for the pattern that is needed\n"))
spacecount=0
for i in range(n,0,-1):
    print(" "*spacecount,end="")
    print("*"*(2*i-1),end="")
    print(" "*spacecount,end="")
    print()
    spacecount+=1
