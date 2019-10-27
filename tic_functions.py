
#defines if am ove is valid or not. 
def move_validation(game_board_input, game_board):

    if game_board_input not in game_board or game_board[game_board_input-1] =='X' or game_board[game_board_input-1] == 'O':
        return True
    else:
        return False


#changes the inputed number to either an X or O depending on the player.
def block_change(player_1_turn, game_board_input, game_board):
    if player_1_turn:
        if game_board_input in game_board:
            game_board[game_board_input-1] = 'X'
    else:
        if game_board_input in game_board:
            game_board[game_board_input-1] = 'O'



#defines if there is a win condition. if there is, game ends. 
def win_condition(game_board):
    if game_board[0] == "X" and game_board[1] == "X" and game_board[2] == "X":
        return True
    if game_board[0] == "X" and game_board[4] == "X" and game_board[8] == "X":
        return True
    if game_board[0] == "X" and game_board[3] == "X" and game_board[6] == "X":
        return True
    if game_board[1] == "X" and game_board[4] == "X" and game_board[7] == "X":
        return True
    if game_board[2] == "X" and game_board[5] == "X" and game_board[8] == "X":
        return True
    if game_board[3] == "X" and game_board[4] == "X" and game_board[5] == "X":
        return True
    if game_board[6] == "X" and game_board[7] == "X" and game_board[8] == "X":
        return True
    if game_board[2] == "X" and game_board[4] == "X" and game_board[6] == "X":
        return True
    if game_board[0] == "O" and game_board[1] == "O" and game_board[2] == "O":
        return True
    if game_board[0] == "O" and game_board[4] == "O" and game_board[8] == "O":
        return True
    if game_board[0] == "O" and game_board[3] == "O" and game_board[6] == "O":
        return True
    if game_board[1] == "O" and game_board[4] == "O" and game_board[7] == "O":
        return True
    if game_board[2] == "O" and game_board[5] == "O" and game_board[8] == "O":
        return True
    if game_board[3] == "O" and game_board[4] == "O" and game_board[5] == "O":
        return True
    if game_board[6] == "O" and game_board[7] == "O" and game_board[8] == "O":
        return True
    if game_board[2] == "O" and game_board[4] == "O" and game_board[6] == "O":
        return True