'''
Given a String s, and a number n, print s n times using recursion
'''
def printer(s,n):
    if n!=0:
        print(s)
        printer(s,n-1)

n=int(input("Enter the number of times the string should be printed"))
s = input("Enter the string")
printer(s,n)

