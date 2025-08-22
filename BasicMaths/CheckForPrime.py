'''
Given a number n, check whether it is a prime number or not.
Input:
5
Output:
5 is a Prime number.
'''
n=int(input("Enter a number to check whether it is a Prime Number\n"))
div=1
for i in range(1,n):
    if n%i==0:
        div=i
if div>1:
    print(n,"is not a Prime number.")
else:
    print(n,"is a Prime number.")