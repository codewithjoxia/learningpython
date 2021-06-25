# Interactive Guessing Game

import random
number = random.randint(10, 100)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('Welcome! '+ player_name+ ' I have a number between 10 and 100: input your guess: ')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))