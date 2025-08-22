'''
Given a number n, check whether n is an Armstrong Number. An Armstrong number is one where the number is equal to the sum of the cubes of its digits.
Input:
370
Output:
370 is an Armstrong Number
________________
370 = 3^3 + 7^3
'''
n=int(input("Enter a number to check whether it is an Armstrong Number\n"))
checker = n
sum=0
while checker>0:
    sum+=(checker%10)**3
    checker//=10
if sum==n:
    print(n,"is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")

