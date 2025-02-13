l1 = list(map(lambda x: x * x, [1,2,3]))
l2 = list(filter(lambda x: x > 3, [1,2,3,4,5,4,3,2,1]))


# print(l1)
# print(l2)

nums = [1,2,3,4,5,6]
# plusOneNums = [x+1 for x in nums] 
oddNums = [x for x in nums if x % 2 == 1] 
print(oddNums)
oddNumsPlusOne = [x+1 for x in nums if x % 2 ==1] 
print(oddNumsPlusOne)