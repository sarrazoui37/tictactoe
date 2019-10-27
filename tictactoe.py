import tic_functions

m_validation = tic_functions.move_validation
b_change = tic_functions.block_change
w_conditions = tic_functions.win_condition


game_board = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]

player_1_turn = True
winner = False

while winner is False:
    print(
        game_board[:3]
    )
    print(
        game_board[3:6]
    )
    print(
        game_board[6:]
    )

    if player_1_turn:
        print('Player 1: ')
    else:
        print('Player 2: ')

    try:
        game_board_input = int(input())
    except:
        print('This move is not valid')
        continue

    m_validation(game_board_input, game_board)

    if m_validation(game_board_input, game_board) == True:
        print('Illegal move')
        continue

    b_change(player_1_turn, game_board_input, game_board)

    # win condition
    if w_conditions(game_board) == True:
        winner = True
        break

    player_1_turn = not player_1_turn


if winner is True:
    print(
        game_board[:3]
    )
    print(
        game_board[3:6]
    )
    print(
        game_board[6:]
    )
    print('You win!')
