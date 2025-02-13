# (I)Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes 
# inputs like height, width and depth from user and then calculate volume of the cube:
# volume = height ∗ width ∗ depth
# After calculating volume of cube, compare it with following ranges and print the relevant label:
# Volume Range Label


h = int(input('Enter height of the box: '))
w = int(input('Enter width of the box: '))
d = int(input('Enter depth of the box: '))
vol= h*w*d
statement=''

if(vol>=0 and vol<=10):
    statement='The label of the box is extra small!'

elif(vol>10 and vol<=25):
    statement='The label of the box is  small!'

elif(vol>25 and vol<=75):
    statement='The label of the box is  medium!'

elif(vol>100 and vol<=250):
    statement='The label of the box is  large!'

elif(vol>250 ):
    statement='The label of the box is extra large!'


print(statement)