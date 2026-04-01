'''
Given a number N, print 1 to N using recursion
'''
def recursionPrinter(i,n):
    if i<=n:
        print(i, end=" ")
        recursionPrinter(i+1, n)

n= int(input("Enter the number n to print 1 to n"))
recursionPrinter(1,n)