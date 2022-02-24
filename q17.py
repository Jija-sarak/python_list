'''1714 ==> [1*, 7, 1*, 4] ==> [2, 7, 2, 4]

12345 ==> [1, 2*, 3, 4*, 5] ==> [1, 4, 3, 8, 5]

891 ==> [8, 9*, 1] ==> [8, 18, 1]'''
a = int(input("enter a number :"))
j = str(a)
sum = 0
i = -(len(j))
s = []
while -i >0:
    if i%2==0:
        n = int(j[i])*2
        if n>9:
            n = n-9
            s.append(n)
            sum = sum+ n
        else:
            s.append(n)
            sum=sum+n
    else:
        m = int(j[i])
        sum = sum+m
        s.append(m)
    i+=1
if sum %10==0:
    print("True")
else:
    print("False")
print(s , sum)