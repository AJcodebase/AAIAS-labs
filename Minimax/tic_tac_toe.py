print("hello from tic-tac-toe")

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