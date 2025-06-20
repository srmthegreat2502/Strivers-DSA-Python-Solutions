'''
Example:
Input: ‘N’ = 3

Output:
1
2 2
3 3 3
'''
n = int(input("Enter the number of rows of the pattern\n"))
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i,end=" ")
    print()