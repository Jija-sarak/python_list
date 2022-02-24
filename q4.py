# List product excluding duplicates.
# 	List = [6,1,3,5,6,3,1]
# 	Output: 60
List1 = [6,1,3,5,6,3,1]
b = []
i = 0
product = 1
while i<len(List1):
    if List1[i] not in b:
        b.append(List1[i])
        product = product*List1[i]
    i+=1
print(product)

