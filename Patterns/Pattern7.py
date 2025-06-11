'''
n=5
    *
   ***
  *****
 *******
*********
'''
n = int(input("Enter the number of rows of the pattern that is needed\n"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print(" "*(n-i),end="")
    print()