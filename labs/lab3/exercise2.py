
# i
file = open('cities.txt', 'at')

while True:
    x = int(input("Press 1 to enter city details, and 2 to close file :  "))
    if(x == 2):
        file.close()
        break
    city_name = input("Enter city name : ")
    city_population = input("Enter population of city : ")
    city_mayor = input("Enter City Mayor : ")
    line = f"{city_name}, {city_population}, {city_mayor} \n"
    file.write(line)


# ii
file = open('student.txt', 'x')

file.write("Now we are AI students")