"""Write a Python program to join two given list of lists of same length, element wise. 
Original lists:
[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
Join the said two lists element wise:
[[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
Original lists:
[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
Join the said two lists element wise:
[['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]"""
# a = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# j = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# s = []
# d = []
# i = 0
# while i < len(j):
#     k = 0
#     while k<len(j[i]):
#         a[i].append(j[i][k])
#         k+=1
#     i+=1
# print(a)

a = [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
j = [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
s = []
d = []
i = 0
while i < len(j):
    k = 0
    while k<len(j[i]):
        a[i].append(j[i][k])
        k+=1
    i+=1
print(a)