import copy
from node import Node
from tree import Tree
from minimax import Minimax

POWER_OF_DISTANCE = 2
WIN_SCORE         = 1000
INFINITY          = 100000
mycolor = 'E'
opcolor = 'E'

def evaluate_board(board,n_rows):
    global mycolor,POWER_OF_DISTANCE,WIN_SCORE
    evaluated = 0
    for i in range(n_rows):
        for cell in board[i]:
            if cell == mycolor:
                evaluated += (n_rows-i)**POWER_OF_DISTANCE
                if i == 0:
                    evaluated += WIN_SCORE
            elif cell != 'E':
                evaluated -= (i+1)**POWER_OF_DISTANCE
                if i == n_rows-1:
                    evaluated -= WIN_SCORE
    return evaluated

class MyNode(Node):
    def setEvaluationFunction(self):
        evaluation = evaluate_board(self.board.board,self.board.n_rows)
        self.utility = evaluation

class MyTree(Tree):
    def makeNode(self, height, board, from_cell=None, to_cell=None):
        node = MyNode(from_cell, to_cell, board)
        self.nodes[height].append(node)
        return node
class AlphaBeta:
    INFINITY  = 100000
    @staticmethod
    def getNextMove(height,board,n_rows,n_cols,is_it_maximizer = True,is_it_first = True,alpha = -INFINITY,beta = INFINITY):
        global mycolor,opcolor
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
                                    #MIN MAX
                                    if is_it_maximizer:
                                        if height == 1:
                                            alpha = max(alpha,evaluate_board(board,n_rows))
                                        else:
                                            val = AlphaBeta.getNextMove(height-1,board,n_rows,n_cols,False,False)
                                            if val > alpha:
                                                alpha = val
                                                from_cell = i,j
                                                to_cell = i+x_move,j+y_move
                                    else:
                                        if height == 1:
                                            beta = min(beta,evaluate_board(board,n_rows))
                                        else:
                                            val = AlphaBeta.getNextMove(height-1,board,n_rows,n_cols,True,False)
                                            if val < beta:
                                                beta = val
                                                ret_x,ret_y = i+x_move,j+y_move
                                    #MIN MAX END
                                    board[i+x_move][j+y_move] = move_backup
                                    board[i][j] = turn_color
        if not is_it_first:
            if is_it_maximizer:
                return alpha
            else:
                return beta
        else:
            return from_cell,to_cell
class Agent:
    def __init__(self, color, opponentColor, time=None):
        global mycolor,opcolor
        mycolor = color
        opcolor = opponentColor
        self.color = color
        self.opponentColor = opponentColor
        self.height = 3

    def move(self,board):
        from_cell,to_cell = AlphaBeta.getNextMove(self.height-1,board.board,board.n_rows,board.n_cols)
        #newBoard = copy.deepcopy(board)
        #newBoard.changePieceLocation(self.color, from_cell, to_cell)

        #print(evaluate_board(newBoard))

        return from_cell, to_cell
