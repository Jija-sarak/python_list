# Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7

# The original list is : [15, 81, 11, 234]
# List Integer Summation : [6,9,2,9]
j = [15, 81, 11, 234]#[12, 67, 98, 34]
a = []
i =  0
while i < len(j):
    sum = 0
    while j[i] > 0:
        k = j[i]%10
        sum=sum+k
        j[i]//=10
    a.append(sum)
    i+=1
print(a)