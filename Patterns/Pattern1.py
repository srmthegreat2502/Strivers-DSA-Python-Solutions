'''Example:
Input: ‘N’ = 3

Output:
* * *
* * *
* * *
'''
n = int(input("Enter the size of the square\n"))
for i in range(n):
    for j in range(n):
        print("* ", end="")
    print()
