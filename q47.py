"""Write a Python program to convert a given list of strings into list of lists. 
Original list of strings:
['Red', 'Maroon', 'Yellow', 'Olive']
Convert the said list of strings into list of lists:
[['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]"""
list1 = ['Red', 'Maroon', 'Yellow', 'Olive']
list2 = []
i = 0
while i < len(list1):
    j = 0 
    s = []
    while j < len(list1[i]):
        s.append(list1[i][j])
        j+=1
    list2.append(s)
    i+=1
print(list2)

