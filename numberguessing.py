# Number Guessing Game
# User asked to input a number
# Number is guessed
# User is told whether the number is correct
# Loops until correct answer
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Please guess a number between 1 and {x}: '))
        if guess > random_number:
            return('Sorry guess again. Number is too high. ')
        elif guess < random_number:
            return('Sorry guess again. Number is too low. ')
    
    print(f'Congratulations you guess the number {random_number} correctly! ')

guess(10)
