'''
n=4
   A
  ABA
 ABCBA
ABCDCBA
'''
n=int(input("Enter the number of rows of the pattern that is needed\n"))
spacecount = n-1
for i in range(0,n):
    alpha="A"
    print(" "*spacecount,end="")
    for j in range(0,i+1):
        print(alpha,end="")
        alpha = chr(ord(alpha)+1)
    alpha = chr(ord(alpha)-2)
    for j in range(i-1,-1,-1):
        print(alpha,end="")
        alpha = chr(ord(alpha)-1)
    spacecount-=1
    print()
