# Convert Character Matrix to single String;
# 	The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest
list1 = [['g','f','g'],['i','s'],['b','e','s','t']]
j = 0
while j < len(list1):
    k = 0
    while k<len(list1[j]):
        print(list1[j][k],end="")
        k+=1
    j+=1
print()
