"""Write a Python program to find the last occurrence of a specified item in a given list.
Original list:
['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
Last occurrence of f in the said list:
7
Last occurrence of c in the said list:
15
Last occurrence of k in the said list:
14
Last occurrence of w in the said list:
12""" 
a = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
d = []
i = 0 
while i < len(a):
    c = 0
    j = 0 
    while j < len(a):
        if a[i]==a[j]:
            c=j
        j+=1
    if a[i] in d:
        i+=1
        continue
    d.append(a[i])      
    print(a[i],"=",c )