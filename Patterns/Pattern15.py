'''
n=3
A B C
A B
A
'''
n=int(input("Enter the number of rows of the pattern that is needed\n"))
for i in range(0,n):
    alpha='A'
    for j in range(n-i,0,-1):
        print(alpha,end=" ")
        alpha=chr(ord(alpha)+1)
    print()