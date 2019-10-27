   move_validation()

    if game_board_input not in game_board:
        print('Illegal move')
        continue
    if game_board[game_board_input-1] =='X' or game_board[game_board_input-1] == 'O':
        print('Illegal move')
        continue
    
    if player_1_turn:
        if game_board_input in game_board:
            game_board[game_board_input-1] = 'X'
    else:
        if game_board_input in game_board:
            game_board[game_board_input-1] = 'O'

    player_1_turn = not player_1_turn


if player_1_turn:
        if game_board_input in game_board:
            game_board[game_board_input-1] = 'X'
    else:
        if game_board_input in game_board:
            game_board[game_board_input-1] = 'O'