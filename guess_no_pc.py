# Done by Carlos Amaral (2021/01/02)

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Please, guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too low!')
        elif guess > random_number:
            print('Too high!')
        else:
            print(f'Correct, the random_number is {random_number}!! Congratulations :)')


guess(10)

