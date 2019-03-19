import copy
from node import Node
from tree import Tree
from minimax import Minimax

POWER_OF_DISTANCE = 2
WIN_SCORE         = 1000
mycolor = 'E'

def evaluate_board(board):
    global mycolor,POWER_OF_DISTANCE,WIN_SCORE
    evaluated = 0
    for i in range(board.n_rows):
        for cell in board.board[i]:
            if cell == mycolor:
                evaluated += (board.n_rows-i)**POWER_OF_DISTANCE
                if i == 0:
                    evaluated += WIN_SCORE
            elif cell != 'E':
                evaluated -= (i+1)**POWER_OF_DISTANCE
                if i == board.n_rows-1:
                    evaluated -= WIN_SCORE
    return evaluated

class MyNode(Node):
    def setEvaluationFunction(self):
        evaluation = evaluate_board(self.board)
        self.utility = evaluation

class MyTree(Tree):
    def makeNode(self, height, board, from_cell=None, to_cell=None):
        node = MyNode(from_cell, to_cell, board)
        self.nodes[height].append(node)
        return node

class Agent:
    def __init__(self, color, opponentColor, time=None):
        global mycolor
        mycolor = color
        self.color = color
        self.opponentColor = opponentColor
        self.height = 3

    def move(self,board):
        gameTree = MyTree(board, self.color, self.opponentColor, self.height)
        from_cell, to_cell = Minimax.calNextMove(gameTree, self.height)

        #newBoard = copy.deepcopy(board)
        #newBoard.changePieceLocation(self.color, from_cell, to_cell)

        #print(evaluate_board(newBoard))

        return from_cell, to_cell
