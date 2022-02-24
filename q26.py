'''Our task is to print the element which occurs 3 consecutive times in a Python list.
Example:
Input: [4, 5, 5, 5, 3, 8]
Output: 5
Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
Output: 1, 22'''
j = [4, 5, 5, 5, 3, 8]#[1, 1, 1, 64, 23, 64, 22, 22, 22]
i = 1
c = 0
c1=0
while i < len(j):
    if j[i]==j[c]:
        c1+=1
    else:
        c1=c1-c1
    if c1>=2:
        print(j[c])
    c+=1
    i+=1

