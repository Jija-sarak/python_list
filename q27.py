# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# Examples:
# Input: [1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# Input: [0, 9, 5]
# Output:
# 0 9 5
# 0 5 9
# 9 0 5
# 9 5 0
# 5 0 9
# 5 9 0
# A = [1,2,3]
# i = 0
# while i <len(A):
#     j = 0
#     while j<len(A):
#         k = 0
#         while k<len(A):
#             if i!=j and j!=k and i!=k:
#                 print(A[i],A[j],A[k])
#             k+=1
#         j+=1
#     i+=1           

a = [1,"apple",3,4,"mango"]
a[1]=True
print(a)
