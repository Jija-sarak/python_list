# Find the First Maximum, Second maximum, Third maximum number from the List.
j = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
first_max = 0
i = 0
while i < len(j) :
    if j[i]>first_max:
        first_max = j[i]
    i+=1
print(first_max)
second_max = 0
k = 0
while k < len(j):
    if j[k]>second_max:
        if first_max != j[k]:
            second_max=j[k]
    k+=1
print(second_max)
third_max = 0
k = 0
while k < len(j):
    if j[k]>third_max:
        if second_max != j[k] and first_max != j[k]:
            third_max=j[k]
    k+=1
print(third_max)
