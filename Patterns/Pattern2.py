'''Example:
Input: ‘N’ = 3

Output:
*
* *
* * *
'''
n = int(input("Enter number of rows of the pattern\n"))
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print()