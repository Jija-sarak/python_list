# The task is to perform the operation of removing all the occurrences of a given item/element present in a list.
# Input :
# 1 1 2 3 4 5 1 2
# 1
# Output :
# 2 3 4 5 2
# Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1.
# After removing the item, the output list is [2, 3, 4, 5, 2]
# Input :
# 5 6 7 8 9 10
# 7
# Output :
# 5 6 8 9 10
j = int(input("enter a len of list :"))
list1 = []
i = 0
while i < j:
    list1.append(int(input("enter a number:")))
    i+=1
print(list1)
a=int(input("enter a element:"))
for k in list1:
    if a in list1:
        list1.remove(a)
print(list1)

# j = int(input("enter a len of list :"))
# list1 = []
# i = 0
# while i < j:
#     list1.append(int(input("enter a number:")))
#     i+=1
# print(list1)
# for k in list1:
#     if 7 in list1:
#         list1.remove(7)
# print(list1)