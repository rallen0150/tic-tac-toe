def createBoard(board):
    print("    0   1   2")
    print("0     |   |   ")
    print(" " + board[00] + "    |  " + board[01] + "|  " + board[02])
    print("   ---+---+---")
    print("1     |   |   ")
    print(" " + board[10] + "    |  " + board[11] + "|  " + board[12])
    print("   ---+---+---")
    print("2     |   |   ")
    print(" " + board[20] + "    |  " + board[21] + "|  " + board[22])



my_board = [["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]]

createBoard(my_board)
# for row in my_board:
#     print(*row)

# xx_input = input("Player X it's your turn!\nEnter a row number(0-2): ")
# xy_input = input("Enter a column number(0-2): ")
#
# def player_X(xx_input, xy_input):
