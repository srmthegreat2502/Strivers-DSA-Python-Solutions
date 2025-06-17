'''
n=3
A
A B
A B C
'''
n = int(input("Enter the number of the pattern that is needed\n"))
for i in range(0,n):
    al='A'
    for j in range(0,i+1):
        print(al,end=" ")
        al=chr(ord(al)+1)
    print()