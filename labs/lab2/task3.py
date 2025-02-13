#    (iii)The program must prompt the user for a username and password. The program should 
#    compare the password given by the user to a known password. If the password matches, the 
#    program should display “Welcome!” If it doesn’t match, the program should display “I don’t 
#    know you.
#    Note: the password should not be case sensitive and it’s value is abc$123 or ABC$123

passwordsmall='abc$123'
passwordlarge='ABC$123'
userName='Nabeel'

check_user= input("Enter your username: ")

if(check_user==userName):

    check_password =input("Alright Nabeel , now Enter your password: ")
    if(check_password==passwordsmall or check_password==passwordlarge ):
        print("Welcome!")
    else:
        print("I don't know you!, wrong password!")

else:
    print("I don't know you!, wrong name!")

