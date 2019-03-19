import copy
from node import Node
from tree import Tree
from minimax import Minimax

POWER_OF_DISTANCE = 2
WIN_SCORE         = 1000
INFINITY          = 100000
mycolor = 'E'
opcolor = 'E'

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
class AlphaBeta:
    INFINITY  = 100000
    @staticmethod
    def getNextMove(height,board,n_rows,n_cols,is_it_maximizer = True,alpha = -INFINITY,beta = INFINITY):
        global mycolor,opcolor
        move_backup = 'E'
        turn_color = mycolor if is_it_maximizer else opcolor
        x_move = 1 if turn_color == 'W' else -1
        for i in range(n_rows):
            for j in range(n_cols):
                if(board[i][j] == turn_color):
                    if 0<=i+x_move<n_rows:
                        for y_move in range(-1,2):
                            if 0<=j+y_move<n_rows:
                                if y_move == 0 and board[i+x_move][j+y_move] != 'E':
                                    pass
                                else:
                                    move_backup = board[i+x_move][j+y_move]
                                    board[i+x_move][j+y_move] = turn_color
                                    board[i][j] = 'E'
                                    #Complete In Here
                                    board[i+x_move][j+y_move] = move_backup
                                    board[i][j] = turn_color
class Agent:
    def __init__(self, color, opponentColor, time=None):
        global mycolor,opcolor
        mycolor = color
        opcolor = opponentColor
        self.color = color
        self.opponentColor = opponentColor
        self.height = 3

    def move(self,board):
        AlphaBeta.getNextMove(self.height,board.board,board.n_rows,board.n_cols)
        gameTree = MyTree(board, self.color, self.opponentColor, self.height)
        from_cell, to_cell = Minimax.calNextMove(gameTree, self.height)

        #newBoard = copy.deepcopy(board)
        #newBoard.changePieceLocation(self.color, from_cell, to_cell)

        #print(evaluate_board(newBoard))

        return from_cell, to_cell
