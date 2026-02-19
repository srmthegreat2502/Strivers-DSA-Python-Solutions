'''
Given an array nums of size n which may contain duplicate elements.
Return a list of pairs where each pair contains a unique element from the array and its frequency in the array.
You may return the result in any order, but each element must appear exactly once in the output.

The Brute Force Solution can be implemented by using two arrays: the provided array, and the visited array.
We can iterate through every element in the array, one by one, counting the frequency.
If the element in the array matches the one being counted, the index is marked as visited in the visited array.
'''

n=int(input("Enter the number of elements in the array"))
array=[]
d = {}
for i in range(0,n):
    num = int(input("Enter the number"))
    array.append(num)
    freq = d.get(num, 0)
    d[num] = freq+1

print("The array is ",array)
print("The frequencies are",d)
