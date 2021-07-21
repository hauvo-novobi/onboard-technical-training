# String File
# ===

# Given a text file, `text.txt`, with the following content

# ```
# lorem ipsum dolor sit amet consectetur adipiscing elit sed do
# eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim
# ad minim veniam quis nostrud exercitation ullamco laboris nisi ut
# aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit
# in voluptate velit esse cillum dolore eu fugiat nulla pariatur
# excepteur sint occaecat cupidatat non proident sunt in culpa qui
# officia deserunt mollit anim id est laborum
# ```

# Read this file using python, find those words that appear more than 1 time, and save these words to a new file, separated by comma.

# Extras:
# - Print out the count of appearence for each word.
# - Allow user to input a word, check if the word is in the file. If yes, print the times that the word appear, or print out a message saying it does not exist if no.
# - Print the first 100 characters of the string.

def read_file_as_content_and_words(path):
    from functools import reduce
    file = open(path,'r')
    all_content = file.read()
    file.close()
    
    file = open(path,'r')
    content = file.readlines()
    file.close()
    
    words = list(reduce(lambda x,y: x + y.split(" "), content, []))
    return all_content, words
    
def save_over2times_words(words, outpath):
    over2times_words = set(w for w in words if words.count(w) > 1)
    over2times_content = ','.join(over2times_words)
    f = open(outpath,'w')
    f.write(over2times_content)
    f.close()
    print('Save the words that appear more than 1 time successfully.')
def print_appearence_count(words):
    from collections import Counter
    count = Counter(words)
    print('The count of appearence for each word:')
    print(dict(count))
def input_and_check_word_in_file(words):
    from collections import Counter
    count = Counter(words)
    input_word = input('Input a word to check: ')
    if input_word in count:
        print('The word appear', count[input_word], 'times')
    else:
        print('The word does not exist')
def print_first_100_characters(content):
    print('The first 100 characters of the string:', content[:100])
    

if __name__ == '__main__':
    content, words = read_file_as_content_and_words('text.txt')
    save_over2times_words(words, 'over2times_words.txt')
    # Ask user for input or to just execute the chosen function
    print('The program have 3 extras option:')
    print('1 - Print out the count of appearence for each word.')
    print('2 - Allow user to input a word, check if the word is in the file.')
    print('3 - Print the first 100 characters of the string.')
    
    while True:
        selection = input('Choose your selection (1, 2, 3 or exit): ')
        if selection == 'exit':
            break
        elif selection == '1':
            print_appearence_count(words)
        elif selection == '2':
            input_and_check_word_in_file(words)
        elif selection == '3':
            print_first_100_characters(content)
        else:
            continue
        is_continue = input('Do you want to use another feature?(Enter `y` to continue): ')
        if is_continue == 'y':
            continue
        else:
            break