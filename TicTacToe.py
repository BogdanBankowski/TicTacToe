from os import system, name
from termcolor import colored
import random


def print_menu():
    system('clear')

    print(colored("TICTACTOE".center(100), "red"))
    print()
    print("Wybierz tryb rozgrywki poprzez wpisanie 1,2 lub 3 i zatwierdzenie Enterem:".center(100))
    print()
    print("1. Player vs. Player".center(100))
    print("2. Player vs. CPU   ".center(100))
    print("3. CPU    vs. Player".center(100))

    Input_Done = False
    while not Input_Done:
        Choice = input()
        if (Choice == '1' or Choice == '2' or Choice == '3'):
            Input_Done = True
        else:
            print("Brak takiej opcji")
    return Choice

# ---------------------------------------------------------------------------------------------------

def print_board():
    global turn 
    turn +=1
    system('clear')
    print("                                  _" ,
          board_state[0],"_|","_",board_state[1],"_|","_",board_state[2],"_")
    print("                                  _" ,
          board_state[3],"_|","_",board_state[4],"_|","_",board_state[5],"_")
    print("                                  _" ,
          board_state[6],"_|","_",board_state[7],"_|","_",board_state[8],"_")
# ---------------------------------------------------------------------------------------------------


def if_Won(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for i in winning_combinations:
        if board_state[i[0]] == board_state[i[1]] == board_state[i[2]] == player:
            return True
    return False
# ---------------------------------------------------------------------
def make_move (player):
    if player == X:
        player2 = O
    else:
        player2 = X


    for i in range(9):
        if board_state[i]!=X and board_state[i]!=O:
            board_state[i] = player
            if if_Won(player):
                board_state[i]=i+1
                return i+1
            else:
                board_state[i]=i+1
    for i in range(9):
        if board_state[i] != X and board_state[i] != O:
            board_state[i] = player2
            if if_Won(player2):
                board_state[i]=i+1
                return i+1
            else:
                board_state[i] = i+1
    #srodek wolny
    if board_state[4] != X and board_state[4] != O and not (strategy == 'corner' and turn == 1 and Choice == '3'):
        return 5
    
    #srodek zajety 4 rogi wolne
    if (board_state[4] == X or board_state[4] == O) and ( board_state[0] != X and board_state[0]!=O and board_state[2]!=X and board_state[2]!=O and board_state[6]!=X and board_state[6]!=O and board_state[8]!=X and board_state[8]!=O) and turn == 2:
        return random.choice([1,3,7,9])
    
    if Choice == '2' and turn == 4:
        #srodek i ukos vs ukos - not loosing
        if board_state[4] == player2 and board_state[0] == player2 and board_state[8] == player:
            return random.choice([3,7])
        if board_state[4] == player2 and board_state[2] == player2 and board_state[6] == player:
            return random.choice([1,9])
        if board_state[4] == player2 and board_state[8] == player2 and board_state[0] == player:
            return random.choice([3,7])
        if board_state[4] == player2 and board_state[6] == player2 and board_state[2] == player:
            return random.choice([1,9])
        
        #ukos i ukos vs srodek - not loosing
        if board_state[4]==player and board_state[0] == player2 and board_state[8] == player2:
            return random.choice([2,4,6,8])
        if board_state[4]==player and board_state[2] == player2 and board_state[6] == player2:
            return random.choice([2,4,6,8])
    if Choice == '3' and turn == 3 and strategy == 'center':
        #winning by center - good def , second move  
        if board_state[4] == player and board_state[0] == player2:
            return 9
        if board_state[4] == player and board_state[2] == player2:
            return 7
        if board_state[4] == player and board_state[6] == player2:
            return 3
        if board_state[4] == player and board_state[8] == player2:
            return 1
    
        #winning by center - bad def, second move
    if Choice == '3' and  turn == 3 and strategy == 'center':
        if board_state[4] == player and board_state[1] == player2:
            return 9
        if board_state[4] == player and board_state[3] == player2:
            return 3
        if board_state[4] == player and board_state[5] == player2:
            return 1
        if board_state[4] == player and board_state[7] == player2:
            return 1

        #winning by corners, first move
    if Choice == '3' and turn == 1:
        return random.choice([1,3,7,9])
    
        #winning by corners, second move against center
    if Choice == '3' and turn == 3:
        if board_state[4] == player2 and board_state[0] == player:
            return 9
        if board_state[4] == player2 and board_state[2] == player:
            return 7
        if board_state[4] == player2 and board_state[6] == player:
            return 3
        if board_state[4] == player2 and board_state[8] == player:
            return 1
        
        #extremly stupid oponent
    if turn == 5:
        if board_state[4] == player and board_state [8] == player and board_state[5] == player2:
            return 8
        if board_state[4] == player and board_state [8] == player and board_state[7] == player2:
            return 6
        if board_state[4] == player and board_state [6] == player and board_state[3] == player2:
            return 8
        if board_state[4] == player and board_state [6] == player and board_state[7] == player2:
            return 4
        if board_state[4] == player and board_state [0] == player and board_state[3] == player2:
            return 2
        if board_state[4] == player and board_state [0] == player and board_state[1] == player2:
            return 4
        if board_state[4] == player and board_state [2] == player and board_state[1] == player2:
            return 6
        if board_state[4] == player and board_state [2] == player and board_state[5] == player2:
            return 2

    while True:
        random_move=random.randint(1,9)
        if board_state[random_move-1] == X or board_state[random_move-1] == O:
            continue
        else:
            return random_move

def if_Draw():
    for i in range(9):
        if (board_state[i] != X and board_state[i] != O):
            return False
    return True

def repair_board():
    global turn
    turn = 0
    global strategy
    if strategy =='center':
        strategy = 'corner'
    else:
        strategy = 'center'
    for i in range(9):
        board_state[i] = str(i+1)
X = 'X'
O = 'O'
turn = 0
If_Play = True
strategy = 'center'
while (If_Play == True):
    board_state = ['1','2','3','4','5','6','7','8','9']
    board_size = len(board_state)
    random_correct_X = False
    random_correct_O = False
    Input_Done = False
    Choice = print_menu()
    print_board()
    while(not if_Won(X) and not if_Won(O)):
        while (Input_Done == False):
            if(Choice == '1' or Choice == '2'):
                try:
                    tempX = int(input("Wybierz pole(X):"))
                    if tempX>0 and tempX<10:
                        Pole_Zajete_X = True
                        Input_Done = True
                    else:
                        print("Wybierz pole z mozliwego zakresu")
                except:
                    print("Robisz cos nie tak, sprobuj jeszcze raz!")
            else:
                tempX = make_move(X)
                random_correct_X = False
                Pole_Zajete_X = True
                Input_Done = True
        Input_Done = False

        while (Pole_Zajete_X == True):
            Pole_Zajete_X = False
            if (board_state[tempX-1] != X and board_state[tempX-1] != O):
                board_state[tempX-1] = X
                print_board()
                if(if_Won(X)):
                    print("WYGRAL X !!!")
                    Pole_Zajete_X = False
                    break

            else:
                print("Pole X zajete")
                while (Input_Done == False):
                    try:
                        tempX = int(input("Wprowadz jeszcze raz X:"))
                        Pole_Zajete_X = True
                        Input_Done = True
                    except:
                        print("Robisz cos nie tak, sprobuj jeszcze raz!")
                Input_Done = False
        if(if_Draw() and not if_Won(X)):
            print("Brak mozliwosci dalszych ruchow, REMIS")
            Pole_Zajete_X = False
            break
        if(not if_Won(X) and not if_Draw()):
            while(Input_Done == False):
                if(Choice == '1' or Choice == '3'):
                    try:
                        tempY = int(input("Wybierz pole(O):"))
                    except Exception:
                        print("Robisz cos nie tak, sprobuj jeszcze raz!")
                        continue
                    if tempY > 0 and tempY < 10:
                        Pole_Zajete_O = True
                        Input_Done = True
                    else:
                        print("Wybierz pole z mozliwego zakresu")
                else:
                    tempY=make_move(O)
                    random_correct_O = False
                    Pole_Zajete_O = True
                    Input_Done = True

            Input_Done = False

        while (Pole_Zajete_O == True):
            Pole_Zajete_O = False
            if (board_state[tempY-1] != X and board_state[tempY-1] != O):
                board_state[tempY-1] = O
                print_board()
                if(if_Won(O)):
                    print("WYGRAL O !!!")
                    Pole_Zajete_O = False
                    break
            else:
                print("Pole O zajete")
                while(Input_Done == False):
                    try:
                        tempY = int(input("Wprowadz jeszcze raz O:"))
                        Pole_Zajete_O = True
                        Input_Done = True
                    except Exception:
                        print("Robisz cos nie tak, sprobuj jeszcze raz!")
                Input_Done = False
    if (input("Jesli chcesz grac dalej wpisz 'tak' i wcisnij enter, aby zakonczyc cokolwiek innego:") == 'tak'):
        repair_board()
    else:
        If_Play=False
