# Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
# Iist2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1

j =[-12, 14, 95, 3]#  [2, -7, 5, -64, -14]
i = 0
c = 0
c1 = 0
while i < len(j):
    if j[i]>0:
        c+=1
    else:
        c1+=1
    i+=1
print("pos =",c,"\n""neg =",c1)