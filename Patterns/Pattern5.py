'''
n = 5
* * * * *
* * * *
* * *
* *
*
 */
'''
n = int(input("Enter number of rows of the pattern needed\n"))
for i in range(n,0,-1):
    for j in range(0,i,1):
        print("*",end=" ")
    print()