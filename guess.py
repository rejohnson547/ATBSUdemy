# 05/03/2020
# This is a guess the number game.
import random

print('Hello, what is your name?')

name = input()

print('Well, ' + name + ' I am thinking of a number between')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # this condition is for the correct guess!

if guess == secretNumber:
    print('Good Job, ' + name + ' You guessed my number in ' + str(guessesTaken) + 'guess')
else:
    print('Nope. The number Ii was thinking of was ' + str(secretNumber))
print('You took ' + str(guessesTaken) + ' guesses.')