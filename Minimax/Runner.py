# import tic_tac_toe

# board = tic_tac_toe.initial_state()
# print("Board:", board)
# print("Current player: ", tic_tac_toe.player(board))
# print("Available actions: ", tic_tac_toe.actions(board))

# move = (1,2)

# new_board = tic_tac_toe.result(board, move)
# print("New Board: ")
# for row in new_board:
#     print(row)

import tic_tac_toe
def print_board(board):
    for row in board:
        print(" | ".join(" "if cell is None else cell for cell in row))
        print("---------")


board = tic_tac_toe.initial_state()

print("Initial Board:")
print_board(board)

while True:
    print_board(board)
    if tic_tac_toe.terminal(board):
 
        break
    if tic_tac_toe.player(board) == tic_tac_toe .X:
        print("Your turn")
        
        row = int(input("Enter row (0-2): "))
        if row < 0 or row > 2:
            print("Invalid row. Please enter a value between 0 and 2.")
            continue
        column = int(input("Enter column (0-2): "))
        if column < 0 or column > 2:
            print("Invalid column. Please enter a value between 0 and 2.")
            continue
        move = (row, column)
        board = tic_tac_toe.result(board, move)
    else:
        print("AI is thinking...")
        ai_move = tic_tac_toe.minimax(board)
        board = tic_tac_toe .result(board, ai_move)
print_board(board)
winner = tic_tac_toe.winner(board)
if winner == tic_tac_toe    .X:
 
    print("X wins!")
elif winner == tic_tac_toe.O:
 
    print("O wins!")
else:
    print("Draw!")