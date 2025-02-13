# Make a multiplication table using a loop

table = int(input("Enter the number whose table you want to print: "))
# note : for k syntax me brackets nhi lgaane hoty!
for i in range(1,11):
    print(table,'x',i,'=',table*i)