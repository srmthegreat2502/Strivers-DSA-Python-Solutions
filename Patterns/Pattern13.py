'''
n=4
1
2 3
4 5 6
7 8 9 10
'''
n=int(input("Enter the number of rows of the pattern that is needed\n"))
counter=1
for i in range(0,n):
    for j in range(0,i+1):
        print(counter,end=" ")
        counter+=1
    print()