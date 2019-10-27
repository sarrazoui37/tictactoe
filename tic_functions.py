
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
def win_condition():
    pass