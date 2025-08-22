'''
Given a number n, print the reverse of that number.
In LeetCode, there is a limit given that the number is between -2^31 and 2^31, which is not given here.The problem is called Reverse Integer in Leetcode.
This problem can also be simply solved by converting it into a String, and reversing it. The more logically difficult solution has been solved here.
Input:
2130
Output:
321
'''
n = int(input("Enter a number to reverse it\n"))
sub=n
rev=0
while abs(sub)>0:
    rev=rev*10+abs(sub)%10
    sub = abs(sub)//10
print("The reverse of ",n,"is",rev if n>0 else rev*-1)

