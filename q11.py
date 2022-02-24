# For example, if we give 9119  the function should return  811181, as the  square of 9 is 81 and square of 1  is 1.
j = input("enter a number:")
# for i in j:
#     s=int(i)
#     print(s*s,end="")
# print()
i = 0
a = ""
while i < len(j):
    a=a+str(int(j[i])*int(j[i]))
    i+=1
print(a)