# Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# Output: [1,2,3]
List1 = [1,2,3,1,2,2]
list1 = []
for i in List1:
    if i not in list1:
        list1.append(i)
print(list1)
