import string
import random

# Exercise 1
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
# Extras:
# - Keep the game going until the user types “exit”
# - Keep track of how many guesses the user has taken, and when the game ends, print this out.
def guessing_game():
    sol = random.randint(0, 9)
    inp = input("Enter your guess: ")
    guessing_times = 0
    while 1:
        if inp == 'exit':
            print('exit successfully. You have taken', guessing_times,
                  'guess' if guessing_times == 1 else 'guesses')
            break
        else:
            try:
                number = int(inp)
            except ValueError:
                inp = input(
                    'Please enter a number in the range of [0,9]. Enter a new number: ')
                continue
            guessing_times += 1
            if number == sol:
                print('You guessed exactly right. You have taken',
                      guessing_times, 'guess' if guessing_times == 1 else 'guesses')
                break
            elif number > sol:
                print('You guessed too high')
            else:
                print('You guessed too low')
            inp = input("Enter a new number: ")

# Exercise 2
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.

def generate_password(number_of_letter=16):
    all_leters = string.digits + string.ascii_lowercase + \
        string.ascii_uppercase + string.punctuation
    if number_of_letter < 4:
        return random.sample(all_leters, number_of_letter)
    else:
        obligated_leters = random.choice(string.digits) + \
            random.choice(string.ascii_lowercase) + \
            random.choice(string.ascii_uppercase) + \
            random.choice(string.punctuation)
        result_list = list(obligated_leters +
                        ''.join(random.sample(all_leters, number_of_letter - 4)))
        random.shuffle(result_list)
        res = ''.join(result_list)
        return res


def generate_password_feature():
    print('Generated password is:', generate_password())
    while True:
        is_continue = input('Do you want another passwork?(y/n): ')
        if is_continue == 'y':
            print('New password is:', generate_password())
        elif is_continue == 'n':
            break


if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    print('The program have 2 feature:')
    print('1 - Guess a number between 1 and 9.')
    print('2 - Generate a strong password')
    # result = func(a, b, c=c, d=d)
    while True:
        selection = input('Choose your selection (1 or 2): ')
        if selection == '1':
            guessing_game()
        elif selection == '2':
            generate_password_feature()
        else:
            print("Your input must be 1 or 2. Please enter another")
            continue
        is_continue = input('Do you want to use another feature?(Enter `y` to continue): ')
        if is_continue == 'y':
            continue
        else:
            break
