# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 3+5+9=17. Their absolute difference is 17-15=2
a= [[1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]]
i = 0
sum = 0
s=0
while i < len(a):
    j = 0
    while j < len(a[i]):
        if i==j:
            sum+=a[i][j]
        if i+j==len(a[i])-1:
            s=s+a[i][j]
        j+=1
    i+=1
print("difference",s-sum)