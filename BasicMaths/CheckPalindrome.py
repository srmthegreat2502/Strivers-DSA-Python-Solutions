'''
Given a number n, check whether it is a Palindrome. It is labelled Palindrome Number in LeetCode.
The problem can also be solved by converting it into a String, reversing it, and checking for equality with the original String.
The solution that is logically more difficult is solved here.
Input:
-121
Output:
-121 is not a Palindrome.
'''
n = int(input("Enter a number to check whether it is a Palindrome.\n"))
rev = 0
sub = n
if n<0:
    print(n,"is not a Palindrome")
else:
    while sub>0:
        rev = rev*10+sub%10
        sub//=10
    if rev==n:
        print(n,"is a Palindrome.")
