def mainMenu():
    print('Hello and welcome to Battleships!')
    chose = int(input("1. Single player \n2. Multiplayer\n"))
    if chose == 1:
        singlePlayer()
    elif chose == 2:
        multiPlayer()
    
def singlePlayer():
    print('You have started Singleplayer NOT YET IMPLEMENTED')
    player1 = input('Enter your name: ')

def multiPlayer():
    print('you have started multiplayer')
    player_1 = input("Player 1 input your name: ")
    player_2 = input('Player 2 input your name: ')
    putShip('1')
    putShip('1')
    putShip('2')
    

def printBoard(board):
    print('   A  B  C  D  E  F  G  H  I  J')
    for x in range(10):
        print(x,board[x])


def putShip(whichboard):
    direction = input('Which direction you want to place it? (H for horizontal V for vertical)')
    while direction != 'H' and direction != 'V':
        print('invalid input')
        direction = input('Which direction you want to place it? (H for horizontal V for vertical)')
    
    if direction == 'H':
        print('Tell me the column (A-I) please') 
        column = input('')
    
        while column != 'A' and column != 'B' and column != 'C' and column != 'D' and column != 'E' and column != 'F' \
        and column != 'G' and column != 'H' and column != 'I':

            print('Wrong input try again')
            column = input('')
    else:
        print('Tell me the column (A-J) please') 
        column = input('')
    
        while column != 'A' and column != 'B' and column != 'C' and column != 'D' and column != 'E' and column != 'F' \
        and column != 'G' and column != 'H' and column != 'I' and column != 'J':

            print('Wrong input try again')
            column = input('')

    first_coordinate = ord(column)
    first_coordinate -= 65

    if direction == 'H':
        print('Tell me the row (0-9) please') 
        column = input('')
    
        while column != '0' and column != '1' and column != '2' and column != '3' and column != '4' and column != '5' \
            and column != '6' and column != '7' and column != '8' and column != '9' :

            print('Wrong input try again')
            column = input('')
    else:
        print('Tell me the row (0-8) please') 
        column = input('')
    
        while column != '0' and column != '1' and column != '2' and column != '3' and column != '4' and column != '5' \
            and column != '6' and column != '7' and column != '8':

            print('Wrong input try again')
            column = input('')
        
    second_coordinate = ord(column)
    second_coordinate -= 48

    if whichboard == '1':
        if direction == 'H':
            board_1_ships[second_coordinate][first_coordinate] += 1
            board_1_ships[second_coordinate][first_coordinate+1] += 1
            printBoard(board_1_ships)
        else: 
            board_1_ships[second_coordinate][first_coordinate] += 1
            board_1_ships[second_coordinate+1][first_coordinate] += 1
            printBoard(board_1_ships)
    elif whichboard == '2':
        board_2_ships[second_coordinate][first_coordinate] = 1
        printBoard(board_2_ships)
        
    
        

    
board_1 = [[0 for x in range(10)] for y in range(10)] 
board_1_ships = board_1
board_2 = [[0 for x in range(10)] for y in range(10)]
board_2_ships = board_2

printBoard(board_1)
printBoard(board_1)
putShip('1')




