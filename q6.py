a = [17 ,28 ,30]
b = [99 ,16 ,844]
c = 0
c1 = 0
i = 0 
while i < len(a):
    if a[i]>b[i]:
        c+=1
    if b[i]>a[i]:
        c1+=1
    i+=1
print("a =",c,"b =",c1)
