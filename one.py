import random

def person(x):
    random_number = random.randint(1, x)
    person = 0
    while person != random_number:
        person = int(input(f'Guess a number between 1 and {x}: '))
        if person < random_number:
            print('Sorry, guess again. Too low.')
        elif person > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

person(100)