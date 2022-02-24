'''Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
Original list:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Difference between elements (n+1th - nth) of the said list :
[1, 1, 1, 1, 1, 1, 1, 1, 1]
Original list:
[2, 4, 6, 8]
Difference between elements (n+1th - nth) of the said list :
[2, 2, 2]'''
j = [2, 4, 6, 8]#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = []
i = 1
k = 0
while i<len(j):
    s = j[i]-j[k]
    a.append(s)
    i+=1
    k+=1
print(a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = int(input("enter a number:"))
# print(a[-num:]+a[:-num])