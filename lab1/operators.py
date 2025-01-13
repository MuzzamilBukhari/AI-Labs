# i)
x = 6 
if (type(x) is int):  
  print ("true")  
else:  
  print ("false") 

# output - true
# ii)
x = 7.2 
if (type(x) is not int):  
  print ("true")  
else:  
  print ("false")  

# output - true

# iii)
list1=[1,2,3,4,5]
list2=[6,7,8,9]  
# for item in list1:  
#   if item in list2:  
#     print("overlapping")      
#   else:  
#     print("not overlapping")

# output - not overlapping 5 times

# iv
# a = 5
# a//=3  
# a**=5 
# print('floor divide=',a) 
# print('exponent=',a) 

# NameError: a is not defined

# v)
a = 60 # 60 = 0011 1100    
b = 13 # 13 = 0000 1101  
c = 0    

c = a & b       # 12 = 0000 1100 #  
print("Line 1", c ) 
 
c = a | b       # 61 = 0011 1101 # 
print("Line 2 ", c ) 
 
c = a ^ b       # 49 = 0011 0001 #  shayad xor he
print("Line 3 ", c ) 
 
c = ~a         #-61 = 1100 0011 # negation
print("Line 4", c ) 
 
c = a << 2     # 240 = 1111 0000 # shift left by 2 - multiply by 4
print("Line 5 ", c ); 
 
c = a >> 2     # 15 = 0000 1111  # shift right by 2
print("Line 6 -", c ); 
