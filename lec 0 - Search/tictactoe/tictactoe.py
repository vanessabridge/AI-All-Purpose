"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == O:
                o_count+=1
            elif board[i][j] == X:
                x_count+=1
    if x_count ==0 and o_count ==0: return X
    if x_count > o_count:
        return O
    else: return X
   



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.append((i,j))
    return possible_actions      


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if board[i][j] is not EMPTY:
        raise NameError("INVALID ACTION")
    new_board = deepcopy(board)
    new_board[i][j]=player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check verctical lines
    for i in range(len(board)):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            return board[i][0]
    # Check Horizontal
    for i in range(len(board)):
        if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            return board[0][i]
    if board[0][0]==board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2]==board[1][1] and board[1][1] == board[2][0]:
        return board[0][0]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if actions(board) is  None:
        return True
    
    return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    all_possible_actions = actions(board)
    new_board_score=[]
    for action in all_possible_actions:
        new_board = result(board,action)
        score = utility(new_board)
        new_board_score.append((score,action))
    

def max_value(board):
    return 0

def min_value(board):
    return 0
