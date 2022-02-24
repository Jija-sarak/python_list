"""Write a Python program to compute the average of nth elements in a given list of lists with different lengths.
Original list:
[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
Average of n-th elements in the said list of lists with different lengths:
[4.8, 5.8, 6.8, 8.0, 11.0]"""
list1 = [[0, 1, 2], 
         [2, 3, 4], 
         [3, 4, 5, 6], 
         [7, 8, 9, 10, 11], 
        [12, 13, 14]]
i = 0
s = list1[i]
l = []
while i < len(list1):
    
    