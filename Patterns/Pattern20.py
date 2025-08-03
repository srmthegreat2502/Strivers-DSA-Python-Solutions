'''
n = 3
*         *
* *     * *
* * * * * *
* *     * *
*         *
'''
n=int(input("Enter number of rows of the pattern that is needed\n"))
counter=1
spacecount=2*n-2
for i in range(1,2*n):
    print("* "*counter,end="")
    print("  "*spacecount,end="")
    print("* "*counter)
    if(i<n):
        counter+=1
        spacecount-=2
    else:
        counter-=1
        spacecount+=2

