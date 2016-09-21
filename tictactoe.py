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


def winHorizontal(board, player):
    for row in myBoard:
        if row == ["X", "X", "X"] or row == ["O", "O", "O"]:
            print("Player {} Wins by Horizontal Line!!".format(player))
            end_game = 0
            return end_game
    return 1

def winVertical(board, player):
    if myBoard[0][0] == new_player and myBoard[1][0] == new_player and myBoard[2][0] == new_player:
        print("Player {} Wins by Vertical Line!!".format(new_player))
        end_game = 0
        return end_game
    elif myBoard[0][1] == new_player and myBoard[1][1] == new_player and myBoard[2][1] == new_player:
        print("Player {} Wins by Vertical Line!!".format(new_player))
        end_game = 0
        return end_game
    elif myBoard[0][2] == new_player and myBoard[1][2] == new_player and myBoard[2][2] == new_player:
        print("Player {} Wins by Vertical Line!".format(new_player))
        end_game = 0
        return end_game
    else:
        return 1


def winDiagonal(board, player):
    if myBoard[0][0] == new_player and myBoard[1][1] == new_player and myBoard[2][2] == new_player:
        print("Player {} Wins by Diagonal!".format(new_player))
        end_game = 0
        return end_game
    elif myBoard[0][2] == new_player and myBoard[1][1] == new_player and myBoard[2][0] == new_player:
        print("Player {} Wins by Diagonal!".format(new_player))
        end_game = 0
        return end_game
    else:
        return 1

# The Board code is inspired by the book but wanted to try it as a matrix and not a dictionary
myBoard = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]
# new_board = printBoard(myBoard)


# blank_board = [[" ", " ", " "],
#                [" ", " ", " "],
#                [" ", " ", " "]]

end_game_h = 1
end_game_v = 1
end_game_d = 1
player = ""
turns = 0

while turns < 9 and end_game_h == 1 and end_game_v == 1 and end_game_d == 1:
    new_player = changePlayer(player)
    printBoard(myBoard)
    playerMove(myBoard, new_player)

    end_game_h = winHorizontal(myBoard, new_player)
    end_game_v = winVertical(myBoard, new_player)
    end_game_d = winDiagonal(myBoard, new_player)

    turns += 1

printBoard(myBoard)
