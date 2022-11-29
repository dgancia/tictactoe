import os

board = ["  -  ","  -  ","  -  ",
        "  -  ","  -  ","  -  ",
        "  -  ","  -  ","  -  "]

start = ["=============================",
         "=== Welcome to TicTacToe! ===",
         "============================="]

understandable= []

currentPlayer = "  X  "
winner = None
gameRunning = True

# Game Start

def gameStart(start):
    os.system('cls')
    print("|                                                                                                        |")
    print("|","="*102,"|")
    print("|                                       === Welcome to TicTacToe! ===                                    |")
    print("|","="*102,"|")
    print("|                                                                                                        |")


    inputStart = input("| => Should we should start?(y or n) ")
    

    if(inputStart == "y" or "Y"):  
        print("|","")
        print("|","="*102,"|")
        print("|","| Instruction:                                                                                                     |","|")
        print("|","| The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.|","|")
        print("|","| To place your X or O choose or input to the corresponding number where you want to put your attack               |","|") 
        print("|","| and if you place your attack in a taken place or wrong place, it will proceed to the next player.                |","|")
        print("|","|                                                                                                                  |","|")
        print("|","|                              ( !! A WRONG MOVE CAN GIVE YOUR ENEMY AN ADVANTAGE !! )                             |","|")
        print("|","="*102,"|")
        print("|                                                                                                                          |")
        print("|","                                               === THIS IS THE SAMPLE BOX ===                                          |")
        print("|","                                      ===================           ===================                                |")
        print("|","                                      |  1  |  2  |  3  |           |  -  |  -  |  -  |                                |")
        print("|","                                      -------------------           -------------------                                |")
        print("|","                                      |  4  |  5  |  6  |           |  -  |  -  |  -  |                                |")
        print("|","                                      -------------------           -------------------                                |")
        print("|","                                      |  7  |  8  |  9  |           |  -  |  -  |  -  |                                |")
        print("|","                                      ===================           ===================                                |")
        print("|","")


        understandable = input("| => Is that clear?(y or n) ")

        if(understandable == "y" or "Y"):
            print("|                                                                                                        |")
            print("|","="*102,"|")
            print("|","                                        === Let's play! ===                                            |")
            print("|","="*102,"|")
            print("|                                                                                                        |")
            

        elif(inputStart == "n" or "N"):
            print("|","")
            print("|","="*102,"|")
            print("|","                                == That's ok, take your time :)) ==")
            print("|","="*102,"|")
            print("|","")

            exit()

        else:
            print("|","")
            print("|","="*102)
            print("|","                        == I think that's not the answer I'm looking for :(( ==")
            print("|","="*102)
                
            exit()

    elif(inputStart == "n" or "N"):
        print("|","")
        print("|","="*102)
        print("|","                                   == That's ok, take your time :)) ==")
        print("|","="*102)
        print("|","")

        exit()

    else:
        print("|","")
        print("|","="*102)
        print("|","                           == I think that's not the answer I'm looking for :(( ==")
        print("|","="*102)
            
        exit()

gameStart(start)

# Board

def printBoard(board):

    print("|                                                                                                        |")
    print("|                                        ","="*19,"                                           |")
    print("|                                        ","|" + board[0] + "|" + board[1] + "|" + board[2] + "|","                                           |")
    print("|                                        ","-"*19,"                                           |")
    print("|                                        ","|" + board[3] + "|" + board[4] + "|" + board[5] + "|","                                           |")
    print("|                                        ","-"*19,"                                           |")
    print("|                                        ","|" + board[6] + "|" + board[7] + "|" + board[8] + "|","                                           |")
    print("|                                        ","="*19,"                                           |")
    print("|                                                                                                        |")


# Player Attack Input

def playerInput(board):
    attack = int(input("| ==> Enter a number (1-9) where you want to place your attack: "))
    if attack >= 1 and attack <= 9 and board[attack-1] == "  -  ":
        board[attack-1] = currentPlayer
    else:
        print("|                                                                                                        |")
        print("|","="*102,"|")
        print("|","                       !! That's not possible a player is already in that spot !!                      |")
        print("|","="*102,"|")
        print("|                                                                                                        |")

# Checker

def checkerUpward(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "  -  ":
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] and board[1] != "  -  ":
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != "  -  ":
        winner = board[6]
        return True
        

def checkerSideward(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "  -  ":
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != "  -  ":
        winner = board[3]
        return True

    elif board[2] == board[5] == board[8] and board[2] != "  -  ":
        winner = board[6]
        return True


def checkerDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "  -  ":
        winner = board[0]
        return True

    elif board[2] == board[4] == board[6] and board[2] != "  -  ":
        winner = board[3]
        return True


def checkTie(board):
    global gameRunning
    if "  -  " not in board:
        printBoard(board)
        print("|                                                                                                        |")
        print("|","="*102,"|")
        print("|","                                         === It's a tie ===                                          |")
        print("|","="*102,"|")
        print("|                                                                                                        |")
        
        player_answer = input("Press enter to try again... ")
        gameStart()
        
        gameRunning = False


def checkerWinner():
    global gameRunning
    if checkerDiagonal(board) or checkerSideward(board) or checkerUpward(board):
        print("|                                                                                                        |")
        print("|","="*102,"|")
        print("|",f"                                    === The Winner is",winner,"===                                        |")
        print("|","="*102,"|")
        print("|                                                                                                        |")
        
        player_answer = input("Press enter to go back to menu... ")
        import main
        main()
        gameRunning = False


# Change Players Turn

def nextPlayer():
    global currentPlayer
    if currentPlayer == "  X  ":
        currentPlayer = "  O  "

    else:
        currentPlayer = "  X  "


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkerWinner()
    checkTie(board)
    nextPlayer()
    
    
    

    
    