#     (iii) Try the exercise below:
#     1. Make a program that lists the countries in the set below using a while loop.
#     clist = 
#     ["Canada","USA","Mexico"]

newSet = set()
list=["Canada","USA","Mexico"]
i=1
while(i<=len(list)):
    newSet.add(list[i-1])
    i+=1

print(newSet)