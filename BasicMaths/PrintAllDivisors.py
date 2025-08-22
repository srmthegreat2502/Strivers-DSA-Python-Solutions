'''
Given a number n, print all divisors of n.
Input:
6
Output:
The divisors of 6 are 1, 2, 3, 6
'''
n=int(input("Enter the number to find all its divisors\n"))
print("The divisors of",n,"are",end=" ")
for i in range(1,n+1):
    if n%i==0:
        if(i==n):
            print(str(i)+".")
            break
        print(str(i)+", ",end="")
