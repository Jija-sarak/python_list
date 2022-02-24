# You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12  # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304  # Should return '70000 + 300 + 4'
i = int(input("enter a number :"))
i=str(i)
n = ""
j=0
c=1
while j< len(i):
    l= i[j]+((len(i)-c)*"0")
    if i[j]!= "0":
        n=n+l
        if i[j]!= "0" and j!=len(i)-1:
            n=n+"+"
    c+=1
    j+=1
k=len(n)-1
if n[k]=="+":
    print(n[:k])
else:
    print(n)

# j = ""
# while i > 0:
#     if i>=10000:
#         a=10000
#         n=(i//a)*a
#         j+=str(n)
#     elif i>=1000:
#         a=1000
#         n= (i//a)*a
#         j+=str(n)
#     elif i>=100:
#         a=100
#         n = (i//a)*a
#         j+=str(n)
#     elif i>=10:
#         a=10
#         n=(i//10)*10
#         j+=str(n)
#     i%=a
#     if i>0:
#         j+="+"
#     if i <=9 and i!=0:
#         j+=str(i)
#         break
# print(j)
# def disp():
#     def show():
#         print("my function")
#     print("disp function")
#     show()
# disp()
