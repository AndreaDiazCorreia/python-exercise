"""
    The code allows the user to play a game of rock-paper-scissors against the computer and determines
    the winner.
    :return: The function `play()` returns a string indicating the result of the game. It can return one
    of the following three strings:
    - "It's a tie" if the user and computer chose the same option.
    - "You won!" if the user's choice beats the computer's choice.
    - "You lost!" if the user's choice loses to the computer's choice.
    """
import random

def play():
    user = input("What's your choice?'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
def is_win(player, opponent): 
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player== 'p' and opponent == 'r'):
        return True
    

print(play())