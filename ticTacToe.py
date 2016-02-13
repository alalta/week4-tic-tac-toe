def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])




    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')

   
    
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9):
        printBoard(board) #When you run this program, it will print out a blank tic-tactoe board
        print('Turn for ' + turn + '. Move on which space?') #It's the starting player's turn and asks where they want to move
        move = input() #Enter the space you want to move in
        board[move] = turn #swaps the active player 
        if( checkWinner(board, 'X') ): #Checks to see if player X won
            print('X wins!') # if player X has won, it prints "X wins!"
            break
        elif ( checkWinner(board, 'O') ): #Checks to see if player O won
            print('O wins!') # If player O has won, it prints "O wins!"
            break
    
        if turn == 'X': #if it is player "X" turn then next will be player "O"
            turn = 'O' #moves on to next turn 
        else:
            turn = 'X' #moves on to next turn
        
    printBoard(board)
    
