# Given the start and end of a range, write a Python program to print all negative numbers in a given range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1

# Input: start = -3, end = 4
# Output: -3, -2, -1
start = -int(input("enter a number :"))
end = int(input("enter a number :"))
while start<5:
    if start<0 and start!= 0-1:
        print(start,end=", ")
    if start==0-1:
        print(start)
    start+=1