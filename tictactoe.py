def printBoard(board):
    print("   0   1   2")
    print("0  " + board[0][0] + '  | ' + board[0][1] + ' | ' + board[0][2])
    print('   ---+---+---')
    print("1  " + board[1][0] + '  | ' + board[1][1] + ' | ' + board[1][2])
    print('   ---+---+---')
    print("2  " + board[2][0] + '  | ' + board[2][1] + ' | ' + board[2][2])


def changePlayer(player):
    if turns % 2 == 0:
        player = "X"
    else:
        player = "O"
    return player


def playerMove(board, player):
    player_move_row = int(input('Player {}'.format(new_player) + ', Pick a row(0-2): '))
    player_move_column = int(input('Pick a column(0-2): '))
    while myBoard[player_move_row][player_move_column] != ' ':
        player_move_row = int(input("Invalid Move! Try another row: "))
        player_move_column = int(input('Pick a column: '))
    myBoard[player_move_row][player_move_column] = new_player


# The Board code is inspired by the book but wanted to try it as a matrix and not a dictionary
myBoard = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]


player = ""
turns = 0

while turns < 9:
    new_player = changePlayer(player)
    printBoard(myBoard)
    playerMove(myBoard, new_player)

    turns += 1
printBoard(myBoard)
