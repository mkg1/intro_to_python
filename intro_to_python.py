# print('hello world')
# y = input('Enter a number: ')
# x = type("what is this?")
# print y
# print x
#
# # List & dictionaries - data storage types
# todo_list = ['buy groceries', 'clean kitchen', 'make bed']
# print todo_list
#
# # dictionary
# dictionary = {'age': 29, 'favorite food': 'falafel', 'name': 'molly'}
# print dictionary['age']
#
# dictionary['age'] = 32
# print dictionary

import random
random_number = random.randint(1,100)
print random_number

while True:
    try:
        user_guess = int(input('Guess a number: '))

        if user_guess == random_number:
            print("you got it!")
            break
        elif user_guess < random_number:
            print('you guessed too low, guess again')
        elif user_guess > random_number:
            print('you guessed too high, guess again')
        else:
            print('wrong! guess again')
    except:
        print('please enter a real number')
