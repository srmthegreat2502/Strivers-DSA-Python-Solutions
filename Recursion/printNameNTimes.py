'''
Print your name n times using recursion. similar to PrintSomethingNTimes
'''

def recprint(s,n):
    if(n!=0):
        print(s)
        recprint(s,n-1)

s = input("Enter your name")
n = int(input("Enter the number of times to print your name"))
recprint(s,n)