# Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.
a =  [1, 2, 2, 5, 8, 4, 4, 8]
j = []
count = 0
i = 0
while i < len(a):
    if a[i] not in j:
        j.append(a[i])
        count+=1
    i+=1
print(count)
