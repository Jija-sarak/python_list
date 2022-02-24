'''Given a List, extract all elements whose frequency is greater than K.
Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
Output: [4, 3]
Explanation: Both elements occur 4 times.
Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
Output: [4, 3, 6]
Explanation: Occur 4, 3, and 3 times respectively.'''
# j = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# a = []
# i = 0
# while i < len(j):
#     k = 0
#     c=0
#     while k < len(j):
#         if j[i]==j[k]:
#             c+=1
#         k+=1
#         if c>3:
#             if j[i] not in a:
#                 a.append(j[i])
#     i+=1
# print(a)

# j = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# a = []
# i = 0
# while i < len(j):
#     k = 0
#     c=0
#     while k < len(j):
#         if j[i]==j[k]:
#             c+=1
#         k+=1
#         if c>2:
#             if j[i] not in a:
#                 a.append(j[i])
#     i+=1
# print(a)
# a = int(input("enter a number :"))
# s = str(a)
# if s[1]=="3":
#     print("yes")
# else:
#     print("no")

# i = 0
# while i < 5:
#     j = 0
#     while j < 5-i:
#         print(" ",end="")
#         j+=1
#     k = 0
#     while k <i:
#         print("*",end="")
#         k+=1
#     print()
#     i+=1

# a= int(input("enter a number"))
# i = 2
# while i <=100:
#     j = 2
#     c=0
#     while j<=100:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==1:
#         print(i)
#     i+=1
# u  =int(input("enter a number:"))
# a = [1,2,3,4,5,6,7,8,9,10]
# s = []
# i = 0
# c=1
# while i<len(a):
#     n = [a[i],a[c]]
#     s.append(n)
#     i+=2
#     c+=2
# print(s)

