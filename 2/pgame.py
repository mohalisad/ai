from RandomMinimaxAgent import RandomMinimaxAgent
from agent import Agent
from board import Board
from graphicalBoard import GraphicalBoard
import time

def switchTurn(turn):
    if turn == 'W':
        return 'B'
    return 'W'

def my_print(board):
    for i in range(-1,-7,-1):
        print(' '.join(board.board[i]))
    print("██████████████")
def play(white, black, board):
    turn = 'W'
    while not board.finishedGame():
        my_print(board)
        if turn == 'W':
            inp = [int(x) for x in input().split()]
            from_cell, to_cell = (inp[1]-1,inp[0]-1), (inp[3]-1,inp[2]-1)
        elif turn == 'B':
            from_cell, to_cell = black.move(board)
        else:
            raise Exception
        board.changePieceLocation(turn, from_cell, to_cell)
        turn = switchTurn(turn)


if __name__ == '__main__':
    board = Board(6, 6, 2)
    white = RandomMinimaxAgent('W', 'B')
    you = Agent('B', 'W')
    play(white, you, board)
