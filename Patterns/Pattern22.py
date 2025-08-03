'''
n = 4
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''
n=int(input("Enter the number for building the square\n"))
for i in range(0,2*n-1,1):
    for j in range(0,2*n-1,1):
        top = i
        bottom = 2*n-1-1-i
        left = j
        right = 2*n-1-1-j
        minimal = min(min(top,bottom),min(right,left))
        print(n-minimal,end=" ")
    print()