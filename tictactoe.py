
# The Board code is inspired by the book to use it as a dictionary
theBoard = {'00': ' ', '01': ' ', '02': ' ',
            '10': ' ', '11': ' ', '12': ' ',
            '20': ' ', '21': ' ', '22': ' '}

def printBoard(board):
    print("  0 1 2")
    print("0 " + board['00'] + '|' + board['01'] + '|' + board['02'])
    print('  -+-+-')
    print("1 " + board['10'] + '|' + board['11'] + '|' + board['12'])
    print('  -+-+-')
    print("2 " + board['20'] + '|' + board['21'] + '|' + board['22'])

player = 'X'
for i in range(9):
    printBoard(theBoard)
    player_move = input('Player {}'.format(player) + '. Place your spot on a coordinate: ')
    while theBoard[player_move] != ' ':
        player_move = input("Invalid Move! Try another coordinate: ")

    theBoard[player_move] = player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
printBoard(theBoard)
