'''
n=3
C
C B
C B A
'''
n=int(input("Enter the number of rows of the pattern that is needed\n"))
for i in range(0,n):
    alpha = ord("A")+n-1
    for j in range(0,i+1):
        print(chr(alpha),end=" ")
        alpha-=1
    print()