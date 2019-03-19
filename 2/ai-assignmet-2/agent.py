import copy
from node import Node
from tree import Tree
from minimax import Minimax

POWER_OF_DISTANCE = 2
WIN_SCORE         = 1000
INFINITY          = 100000

def evaluate_board(board,n_rows,mycolor):
    global POWER_OF_DISTANCE,WIN_SCORE
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

class AlphaBeta:
    INFINITY  = 100000
    def __init__(self,color, opponentColor):
        self.color = color
        self.opponentColor = opponentColor
    def getNextMove(self,height,board,n_rows,n_cols,is_it_maximizer = True,is_it_first = True,alpha = -INFINITY,beta = INFINITY):
        turn_color = self.color if is_it_maximizer else self.opponentColor
        x_move = 1 if turn_color == 'W' else -1
        ret_flag = False
        if 'B' in board[0]:
            return evaluate_board(board,n_rows,self.color)*height
        if 'W' in board[-1]:
            return evaluate_board(board,n_rows,self.color)*height
        for i in range(n_rows):
            for j in range(n_cols):
                if(board[i][j] == turn_color):
                    if 0<=i+x_move<n_rows:
                        for y_move in range(-1,2):
                            if 0<=j+y_move<n_rows:
                                if board[i+x_move][j+y_move] != turn_color:
                                    if y_move == 0 and board[i+x_move][j+y_move] != 'E':
                                        pass
                                    else:
                                        move_backup = board[i+x_move][j+y_move]
                                        board[i+x_move][j+y_move] = turn_color
                                        board[i][j] = 'E'
                                        #BEGIN
                                        if is_it_maximizer:
                                            if height == 1:
                                                val = evaluate_board(board,n_rows,self.color)
                                            else:
                                                val = self.getNextMove(height-1,board,n_rows,n_cols,False,False,alpha = alpha)
                                            if val > alpha:
                                                alpha = val
                                                if is_it_first:
                                                    from_cell = i,j
                                                    to_cell = i+x_move,j+y_move
                                                if beta <= alpha:
                                                    ret_flag = True
                                        else:
                                            if height == 1:
                                                val = evaluate_board(board,n_rows,self.color)
                                            else:
                                                val = self.getNextMove(height-1,board,n_rows,n_cols,True,False,beta = beta)
                                            if val < beta:
                                                beta = val
                                                if beta <= alpha:
                                                    ret_flag = True
                                        #END
                                        board[i+x_move][j+y_move] = move_backup
                                        board[i][j] = turn_color
                                        if ret_flag:
                                            return alpha if is_it_maximizer else beta
        if not is_it_first:
            return alpha if is_it_maximizer else beta
        else:
            return from_cell,to_cell
class Agent:
    def __init__(self, color, opponentColor, time=None):
        self.color = color
        self.opponentColor = opponentColor
        self.height = 4
        self.myAlphaBeta = AlphaBeta(color,opponentColor)
    def move(self,board):
        from_cell,to_cell = self.myAlphaBeta.getNextMove(self.height,board.board,board.n_rows,board.n_cols)
        return from_cell, to_cell
