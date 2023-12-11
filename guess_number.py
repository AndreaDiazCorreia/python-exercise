#This code defines two functions, guess and computer_guess, to play a number guessing game.

#The guess function allows the user to guess a number between 1 and x, where x is a parameter passed to the function. If the guess is too low or too high, the function provides feedback and prompts the user to guess again. Once the correct number is guessed, a congratulatory message is displayed.

#The computer_guess function allows the computer to guess the user's number. It uses a binary search algorithm to narrow down the range of possible numbers until the correct number is guessed. The function prompts the user for feedback on each guess (too high, too low, or correct) and adjusts the range accordingly. Once the correct number is guessed, a congratulatory message is displayed. In this code, computer_guess is called with an argument of 10 to play the game with a range of numbers from 1 to 10.

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    
    print(f"Yay, congrats. You have guessed the number {random_number} correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
         if low != high:
            guess = random.randint(low, high)
         else:
            guess = low
         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
         if feedback == 'h':
             high = guess - 1
         elif feedback == 'l':
             low = guess + 1
    
    print(f'Yay! The computer guessed your number, {guess}, correctly!')
             

computer_guess(10)