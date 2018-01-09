# Input random generator
import random

# make the guess infinite
guessUsed = 0

# greeting message
print('Greetings Human! Can I get your name?')
name = input()

# generate the number
numbers = random.randint(1,50)

# give em a guessing message to start
print('Well ' + name + ' get ready to guess some numbers....')
print('Guess a number between 1 - 50')

# limit the guesses to 10

while guessUsed < 10:
    print('What is it?')
    guess = input()
    guess = int(guess)

    guessUsed = guessUsed + 1 # makes sure the guess go up by 1

    # rules to see if its higher or lower
    if guess < numbers:
        print('Ah, way too low buddy.')

    if guess > numbers:
        print('Higher than I expected. Go lower!')

    if guess == numbers:
        break
# What if i got it right

if guess == numbers:
    guessUsed = str(guessUsed)
    print('Huh, I did not think you had it in you. Good stuff, you got the answer in ' + guessUsed + ' guesses!')

if guess != numbers:
    number = str(guessUsed)
    print('RIP. The number was ' + numbers + ".")

