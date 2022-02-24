"""Write a Python program to remove the last N number of elements from a given list. 
Original lists:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
Remove the last 3 elements from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
Remove the last 5 elements from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
Remove the last 1 element from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]"""
j = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# i = -len(j)
# while -i >= -(-1):
#     if -i <= -(-3):
#         j.pop(i)
#     i+=1
# print(j)

# i = -len(j)
# while -i >= -(-1):
#     if -i <= -(-5):
#         j.pop(i)
#     i+=1
# print(j)

i = 0
while i <len(j):
    if i == len(j)-1:
        j.pop(i)
    i+=1
print(j)