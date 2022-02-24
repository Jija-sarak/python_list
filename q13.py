"""Write a Python program to create a list reflecting the modified run-length encoding from 
a given list of integers or a given list of characters. 
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Original String:
aabcddddadnss
List reflecting the modified run-length encoding from the said string:
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]"""
list1 = "aabcddddadnss"#[1, 1, 2, 3, 4, 4, 5, 1]
new = []
i = 0
c = 1
k = 1
while k < len(list1):
    if list1[i]==list1[k]:
        c+=1
        a = [c,list1[k]]
        if k == len(list1)-1:
            new.append(a)
    else:
        if a not in new:
            new.append(a)
        if k == len(list1)-1:
            new.append(list1[k])
        elif list1[k]!=list1[k+1]:
            new.append(list1[k])
        c=1
    k+=1
    i+=1
print(new)