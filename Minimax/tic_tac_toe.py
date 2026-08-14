import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]  
    ]

def player(board):
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves



def result(board, action):
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    for i in range(3):
        if board[i][0] != EMPTY:
            if board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
 
    for j in range(3):
        if board[0][j] != EMPTY:
            if board[0][j] == board[1][j] == board[2][j]:
                return board[0][j]
    if board[0][0] != EMPTY: 
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
    # Check second diagonal
    if board[0][2] != EMPTY:
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
    return None
 
 
 
 
 
def terminal(board):
    # Someone won
    if winner(board) is not None:
        return True 
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False 
    return True
 
 
 
 
 
def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_value(new_board)
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    else:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_value(new_board)
            if score < best_score:
                best_score = score
                best_action = action
        return best_action
 
 
 
 
 
def minimax_value(board):
    if terminal(board):
        return utility(board)
    if player(board) == X:
        best_score = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_value(new_board)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_value(new_board)
            best_score = min(best_score, score)
        return best_score
 