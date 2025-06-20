'''
n=3
A
B B
C C C
'''
n=int(input("Enter the number of rows of the pattern that is needed\n"));
alpha='A'
for i in range(0,n):
    for j in range(0,i+1):
        print(alpha, end=" ")
    alpha = chr(ord(alpha)+1)
    print()