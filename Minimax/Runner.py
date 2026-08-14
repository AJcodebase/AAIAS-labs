import tic_tac_toe

board = tic_tac_toe.initial_state()
print("Board:", board)
print("Current player: ", tic_tac_toe.player(board))
print("Available actions: ", tic_tac_toe.actions(board))

move = (1,2)

new_board = tic_tac_toe.result(board, move)
print("New Board: ")
for row in new_board:
    print(row)