# User Input
# ===

# # Exercise 1

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# - Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
# - Print out that many copies of the previous message on separate lines. (Hint: the string "\n" a.k.a newline, is the same as pressing the ENTER button)
from datetime import datetime
    
def enter_and_check_is_number():
    while True:
        try:
            variable = int(input())
            if variable <= 0:
                raise Exception()
            else:
                return variable
        except:
            print("Your input must be a positive numbers. Please enter another: ", end='')
            continue


def year_when_100_year_olds():
    name = input('Enter your name: ')

    print('Enter your age: ', end='')
    age = enter_and_check_is_number()

    year100yearolds = datetime.today().year + 100 - age
    result = 'Hi Hau. You will turn 100 years old in ' + str(year100yearolds)
    print(result)
    
    print('Enter number of repetition: ', end='')
    number = enter_and_check_is_number()

    multiple_result = (result + '\n')*number
    print(multiple_result, end='')
    return result

# # Exercise 2

# Create a program that asks the user to enter their name, their date of birth (mm/dd/yyyy), their gender, their address. After done input all of the above program, allow user to input the following command and print out the corresponding information.
# ```
# $ What would you like to know?
# Available commands are: `name`, `age`, `dob`, `gender`, `address`, `all`
# $ Your name is ...
# $ Your age is ...
# $ Your date of birth is ...
# $ Your gender is ...
# $ Your address is ...
# If user ask for all information, print all the above information at once, in each separated line.
# ```

def get_and_show_info():
    name = input('Enter your name: ')
    print('Enter your age: ', end='')
    age = enter_and_check_is_number()
    while True:
        try:
            dob = input('Enter your date of birth(mm/dd/yyyy): ')
            dob_datetime = datetime.strptime(dob, '%m/%d/%Y').date()
            if dob_datetime > datetime.today().date():
                raise
            break
        except:
            print("Your input must be in the format `mm/dd/yyyy` and not after today. Please enter another.")
            continue
    gender = input('Enter your gender: ')
    address = input('Enter your address: ')
    command = input('What would you like to know?\nAvailable commands are: `name`, `age`, `dob`, `gender`, `address`, `all`.\nEnter your command: ')
    while True:
        if command == 'name':
            print('Your name is', name)
        elif command == 'age':
            print('Your age is', age)
        elif command == 'dob':
            print('Your date of birth is', dob)
        elif command == 'gender':
            print('Your gender is', gender)
        elif command == 'address':
            print('Your address is', address)
        elif command == 'all':
            print('Your name is', name, '\nYour age is', age, '\nYour date of birth is', dob, '\nYour gender is', gender, '\nYour address is', address)
        else:
            command = input('This command is not available. Please enter another: ')
            continue
        break

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    print('The program have 2 feature:')
    print('1 - Telling you the year that you will turn 100 years old.')
    print('2 - Telling you about your infomation')
    # result = func(a, b, c=c, d=d)
    while True:
        selection = input('Choose your selection (1 or 2): ')
        if selection == '1':
            year_when_100_year_olds()
        elif selection == '2':
            get_and_show_info()
        else:
            print("Your input must be 1 or 2. Please enter another")
            continue
        is_continue = input('Do you want to use another feature?(Enter `y` to continue): ')
        if is_continue == 'y':
            continue
        else:
            break