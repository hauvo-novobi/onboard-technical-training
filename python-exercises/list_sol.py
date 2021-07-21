# List
# ===

# # Exercise 1

# Given the following list, print out all the elements that are less than `15`

# ```
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# ```

# Extras:

# - Instead of printing the elements one by one, make a new list that has all the elements less than `15` from this list in it and print out this new list.
# - Write this in one line of Python (Hint: List comprehension).
# - The program allow input a parameter called `threshold`, and return a list that contains only elements from the original list `a` that are smaller than given threshold.
def less_than_threshold(lst, threshold):
    """
    Given the following list, print out all the elements that are less than `threshold`
    """
    result = list(filter(lambda e: e < threshold, lst))
    return result


# ex1_less_than_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 15)
# # Excercise 2

# 

# ```
# a = [1, 2, 1, 8, 5, 3, 89, 21, 34, 55, 13]
# ```

# Extras:
# - Using `filter` function for filtering even/odd numbers

def separate_sorted_even_odd(lst):
    """
    Given a list, print out all the elements in ascending order, and print out 2 separate lines, one is for even numbers and the other is for odd numbers.
    """
    sorted_list = sorted(lst)
    # even_numbers = [i for i in sorted_list if i % 2 == 0]
    # odd_numbers = [i for i in sorted_list if i % 2 != 0]
    even_numbers = list(filter(lambda x: x % 2 == 0, sorted_list))
    odd_numbers = list(filter(lambda x: x % 2 != 0, sorted_list))
    return even_numbers, odd_numbers
# ex2([1, 2, 1, 8, 5, 3, 89, 21, 34, 55, 13])

# Exercise 3
def common_list(first_list, second_list):
    """
    Take two lists, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
    Make sure your program works on two lists of different sizes.
    """
    # return list(set(i for i in first_list if i in second_list))
    return list(set(filter(lambda e: e in second_list ,first_list)))
# print(common_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))


# Exercise 4
def first_last_list(lst, number):
    """
    Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
    The program accept a parameter `n`, make a new list of only the first and the last `n` numbers of the list, in the ascending order. For the given list `a`, if `n` equals or greater than `3`, then the whole list should be printed
    """
    if number*2 >= len(lst):
        return sorted(lst)
    else:
        return sorted(lst[:number] + lst[-number:])
# print(first_last_list([5, 20, 10, 15, 25], 3))
# print(first_last_list([5, 20, 10, 1, 17, 15, 25, 44, 3], 4))

# Exercise 5
def to_unique_list(lst):
    """
    Write a program (function!) that takes a list and returns a new list that contains all the unique elements of the list.
    """
    return list(set(lst))
# Extras:

# - Write two different functions to do this - one using a loop and constructing a list, and another using sets.
if __name__ == '__main__':
    # Ask user for input or to just execute the chosen function
    print('The program have 5 feature:')
    print('1 - Create new list with elements are input element less than threshold')
    print('2 - Separate a list to even and odd, in the ascending order')
    print('3 - Create a list that its elements(unique) is common of two input list')
    print('4 - Make a new list of only the first and last elements of the given list')
    print('5 - Make a new list that contains all the unique elements of the given list')

    # result = func(a, b, c=c, d=d)
    while True:
        selection = input('Choose your selection: ')
        if selection == '1':
            lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
            threshold = 15
            print("Sample input:")
            print('\tlist:', lst)
            print('\tthreshold:', threshold)
            result = less_than_threshold(lst, threshold)
            print('Result:', result)
        elif selection == '2':
            lst = [1, 2, 1, 8, 5, 3, 89, 21, 34, 55, 13]
            print('Sample input:')
            print('\tlist:', lst)
            even_list, odd_list = separate_sorted_even_odd(lst)
            print('Result:')
            print('\tEven list:', even_list)
            print('\tOdd list:', odd_list)
        elif selection == '3':
            list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
            list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            print('Sample input:')
            print('\tlist_1:', list_1)
            print('\tlist_2:', list_2)
            result = common_list(list_1, list_2)
            print('Result:', result)
        elif selection == '4':
            lst = [5, 20, 10, 1, 17, 15, 25, 44, 3]
            number = 3
            print('Sample input:')
            print('\tlist:', lst)
            print('\tnumber:', number)
            result = first_last_list(lst, number)
            print('Result:', result)
        elif selection == '5':
            lst = [1, 55, 1, 34, 89, 89, 2, 3, 5, 8, 13, 21, 34, 55, 89]
            print('Sample input:', lst)
            result = common_list(list_1, list_2)
            print('Result:', result)
        else:
            print("Your input must be in [1,2,3,4,5]. Please enter another")
            continue
        break