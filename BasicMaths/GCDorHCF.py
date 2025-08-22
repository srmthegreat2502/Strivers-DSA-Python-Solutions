'''
Given 2 numbers, n1 and n2, find the Greatest Common Divisor of those two numbers.
Input:
n1=12
n2=18
Output:
The HCF/GCD of the two numbers is 6.
'''
n1=int(input("Enter the first number\n"))
n2=int(input("Enter the second number\n"))
smaller = n1 if n1<n2 else n2
gcd = 1
for i in range(smaller, 0, -1):
    if n1%i==0 and n2%i==0:
        gcd = i
        break
print("The GCD of",n1,"and",n2,"is",gcd)