'''
Given a number n, find out and return the number of digits in that number
Input:
n=123
Output:
The number of digits is 3
'''
n=int(input("Enter the number to find out the number of digits in that number"))
length = 0
number = n
while(number>0):
    number//=10
    length+=1
print("The number of digits in ",n, "is ",length)