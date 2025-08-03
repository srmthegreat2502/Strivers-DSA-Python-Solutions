'''
n = 3
* * * * * *
* *     * *
*         *
* *     * *
* * * * * *
'''
n=int(input("Enter number of rows of the pattern that is needed\n"))
spacecount = 0
counter=n
for i in range(1,2*n):
    print("* "*counter,end="")
    print("  "*spacecount,end="")
    print("* "*counter)
    if(i<n):
        spacecount+=2
        counter-=1
    else:
       spacecount-=2
       counter+=1



