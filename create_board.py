import numpy as np

GRID_R = 6
GRID_C = 9
ms = ''


def display_board(board):
    op_board = str(np.flip(board, 0)).replace('[', ' ')
    op_board = op_board.replace(']', ' ')
    op_board = op_board.replace('\'', ' ')
    op_board = op_board.replace('0', '[   ]')
    op_board = op_board.replace('1', '[ X ]')
    op_board = op_board.replace('2', '[ O ]')
    # print(op_board)
    return (op_board)


def play_board():
    board = np.zeros((GRID_R, GRID_C), dtype=int)
    return board


def is_valid_place(board, column ):

    if board[GRID_R - 1][column] != 0.0:
        global ms
        ms = 'This column is full'

    return board[GRID_R - 1][column] == 0


def is_board_full(board):
    for x in np.nditer(board):
        if x == 0:
            return 1
    return 0


def get_next_open_row(board, column):
    for row in range(GRID_R):
        if board[row][column] == 0:
            return row


def place_discs(board, row, column, discs):
    board[row][column] = discs


def winning_move(board, discs):
    # Horizontal Location
    # All posible starting Positions  , we cannot go 4 location beyond the (GRID_C-3)
    for col in range(GRID_C - 3):
        for row in range(GRID_R):
            if board[row][col] == discs and board[row][col + 1] == discs and board[row][col + 2] == discs and \
                    board[row][col + 3] == discs:
                return True
    # Vertical Locations
    # All posible starting Positions  , we cannot go 4 location beyond the (GRID_R-3)
    for col in range(GRID_C):
        for row in range(GRID_R - 3):
            if board[row][col] == discs and board[row + 1][col] == discs and board[row + 2][col] == discs and \
                    board[row + 3][col] == discs:
                return True
    # Diagonal Upward
    for col in range(GRID_C - 3):
        for row in range(GRID_R - 3):
            if board[row][col] == discs and board[row + 1][col + 1] == discs and board[row + 2][col + 2] == discs and \
                    board[row + 3][col + 3] == discs:
                return True
    # Diagonal Downward
    for col in range(GRID_C):
        for row in range(3, GRID_R):
            if board[row][col] == discs and board[row - 1][col + 1] == discs and board[row - 2][col + 2] == discs and \
                    board[row - 3][col + 3] == discs:
                return True


def player_move(ip, board, turn):
    print('Entered..')
    print('Turn Ip', turn)
    global ms
    ms = ''
    if is_board_full(board) == 0:
        ms += display_board(board)
        ms += '\nBoard is Full..!!!'
        ms += '\n Lest\'s start new game...'
        board = play_board()
        turn = 0

    if turn % 2 == 0:
        column = int(ip)
        if is_valid_place(board, column - 1):
            row = get_next_open_row(board, column - 1)
            place_discs(board, row, column - 1, 1)
            turn += 1
            if winning_move(board, 1):
                ms += display_board(board)
                ms += '\n' + 'Player 1 Won the Game...!!!'
                ms += '\n Lest\'s start new game...'
                board = play_board()
                turn = 0


    else:
        print(ip)
        column = int(ip)
        if is_valid_place(board, column - 1):
            row = get_next_open_row(board, column - 1)
            place_discs(board, row, column - 1, 2)
            turn += 1
            if winning_move(board, 2):
                ms += display_board(board)
                ms += '\n' + 'Player 2 Won the Game...!!!'
                ms += '\n Lest\'s start new game...'
                board = play_board()
                turn = 0


    print('Turn Ip' , turn)

    return board, turn, ms
