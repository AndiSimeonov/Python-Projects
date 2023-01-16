def dis_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_inp():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


import random


def choose_first():
    first_or_second = random.randint(1, 2)
    if first_or_second == 1:
        print("Player 1 goes first!")
    else:
        print("Player 2 goes first!")


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    # position is 0 cuz it won't function properly if its 0-8
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board,
                                                                         position):  # check if you are in the board range
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print("Welcome to Tic Tac Toe!")

while True:
    board = [' '] * 10  # resets board
    player1_marker, player2_marker = player_inp()
    turn = choose_first()
    play_game = input("Do you want to play?: (Y/N): ")
    if play_game.lower() == "y":
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == "Player 1":
            # displaying the board and assigning player choice to a var. and using an if/else to see if the win
            # condition is met or if the board is full, and it's a draw, if it's neither go to player 2's turn
            dis_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            if win_check(board, player1_marker):
                dis_board(board)
                print("Congratulations you win!")
                game_on = False
            else:
                if full_board_check(board):
                    dis_board(board)
                    print("It's a draw...")
                    break
                else:
                    turn = "Player 2"
        else:
            # player 2 turn
            dis_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                dis_board(board)
                print("Player 2 wins!")
                game_on = False
            else:
                if full_board_check(board):
                    dis_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = "Player 1"
    if not replay():
        break
