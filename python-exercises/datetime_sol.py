from datetime import datetime,date,timezone
from pytz import timezone as timezone_pytz
# Exercise 1
# Get the current date, datetime and print out to the screen
def ex1_current_datetime():
    """Get the current date, datetime and print out to the screen"""
    print("\tCurent date: ", date.today())
    print("\tCurent datetime: ", datetime.now())
# Excercise 2
# 
def ex2_convert_timezone():
    """Get the current datetime of the timezone `GMT +7` and convert it into `UTC`, `GMT` and print out to the screen"""
    current_datetime = datetime.now().astimezone()
    print("\tDatetime of `GMT+7`:", current_datetime)
    print("\tDatetime of `UTC`:", current_datetime.astimezone(tz=timezone_pytz("UTC")))
    print("\tDatetime of `GMT`:", current_datetime.astimezone(tz=timezone_pytz("GMT")))

# Exercise 3
# Convert the following date string into date and print out as following format `dd/mm/yyyy`
# 
def ex3_datetime_format():
    """
    Convert the following date string into date and print out as following format `dd/mm/yyyy`
    yyyy-mm-dd
    2021-07-04
    """
    dt_input = '2021-07-04'
    print("\tDate input on `yyyy-mm-dd` format:", dt_input)
    dt = datetime.strptime(dt_input, '%Y-%m-%d')
    print("\t`dd/mm/yyyy` format:",dt.strftime("%d/%m/%Y"))
if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    # result = func(a, b, c=c, d=d)
    features = [
        {
            'order': '1',
            'title': 'Display current date and current datetime',
            'func': ex1_current_datetime
        },
        {
            'order': '2',
            'title': 'Display current datetime of the timezone `GMT+7`, `UTC`, `GMT`',
            'func': ex2_convert_timezone
        },
        {
            'order': '3',
            'title': 'Get the current datetime of the timezone `GMT +7` and convert it into `UTC`, `GMT` and print out to the screen',
            'func': ex3_datetime_format
        },
    ]
    print('This program have', len(features) ,'features:')
    for feature in features:
        print(feature['order'], '-', feature['title'])
    while True:
        selection = input('Choose an feature: ')
        if selection in map(lambda f: f['order'],features):
            choosen_feature = next(filter(lambda f: f['order']==selection,features))
            choosen_feature['func']()
            is_continue = input('Do you want to use another feature?(Enter `y` to continue): ')
            if is_continue == 'y':
                continue
            else:
                break
        else:
            print("Your input must be number of feature. Please enter another")