
"""
    The code defines a Tic Tac Toe game and allows a human player to play against a smart computer
    player.
    
    :param game: The `game` parameter is an instance of the `TicTacToe` class. It represents the current
    state of the Tic Tac Toe game
    :param x_player: The `x_player` parameter is an instance of the `HumanPlayer` class, which
    represents a human player using the 'X' letter in the game
    :param o_player: The `o_player` parameter is an instance of the `SmartComputerPlayer` class, which
    represents the computer player that plays as "O" in the Tic Tac Toe game. This player is a smart
    computer player, meaning it uses a strategy to make its moves instead of choosing randomly
    :param print_game: The `print_game` parameter is a boolean flag that determines whether or not to
    print the game board and moves during the game. If `print_game` is set to `True`, the game board and
    moves will be printed. If `print_game` is set to `False`, the game will, defaults to True (optional)
    :return: The code does not explicitly return anything. However, the `play` function returns the
    letter of the winning player or "It's a tie!" if there is no winner.
    """

import math
import time 
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPLayer
class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    def print_board(self): 
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True 

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print(' ')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'
        
        time.sleep(.8)
        
    if print_game:
        print('It\'s a tie!')
        
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = SmartComputerPLayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)