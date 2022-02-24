'''Write a Python program to find the list with maximum and minimum length.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])'''
j = [[1,3], [1], [5, 7], [9, 11], [13, 15, 17]]
i =0
c=1
s = j[i]
while i < len(j):
    if len(j[i])<len(s):
        s = j[i]
        c+=1
    i+=1
print(s,len(s))

i =0
c=1
s = j[i]
while i < len(j):
    if len(j[i])>len(s):
        s = j[i]
        c+=1
    i+=1
print(s,len(s))