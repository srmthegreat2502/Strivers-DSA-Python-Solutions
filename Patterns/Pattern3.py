'''Example:
Input: ‘N’ = 3

Output:
1
1 2
1 2 3
'''
n = int(input("Enter the number of rows in the pattern"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()