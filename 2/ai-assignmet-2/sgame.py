from RandomMinimaxAgent import RandomMinimaxAgent
from agent import Agent
from board import Board
from graphicalBoard import GraphicalBoard
import time

def switchTurn(turn):
    if turn == 'W':
        return 'B'
    return 'W'


def play(white, black, board):
    turn = 'W'
    while not board.finishedGame():
        if turn == 'W':
            t = time.time()
            from_cell, to_cell = white.move(board)
            print("W:" + str(time.time() - t))
        elif turn == 'B':
            t = time.time()
            from_cell, to_cell = black.move(board)
            print("B:" + str(time.time() - t))
        else:
            raise Exception
        board.changePieceLocation(turn, from_cell, to_cell)
        turn = switchTurn(turn)
    if board.win('W'):
        print('w')
    else:
        print('b')


if __name__ == '__main__':
    for i in range(100):
        board = Board(6, 6, 2)
        white = RandomMinimaxAgent('W', 'B')
        you = Agent('B', 'W')
        play(white, you, board)
