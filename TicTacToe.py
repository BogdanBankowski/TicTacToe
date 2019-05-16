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
    while (Input_Done == False):
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
          pos[0],"_|","_",pos[1],"_|","_",pos[2],"_")
    print("                                  _" ,
          pos[3],"_|","_",pos[4],"_|","_",pos[5],"_")
    print("                                  _" ,
          pos[6],"_|","_",pos[7],"_|","_",pos[8],"_")
# ---------------------------------------------------------------------------------------------------


def if_Won(player):
    winners = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for i in winners:
        if pos[i[0]] == pos[i[1]] == pos[i[2]] == player:
            return True
    return False
# ---------------------------------------------------------------------
def make_move (player):
    if player == X:
        player2 = O
    else:
        player2 = X


    for i in range (9):
        if pos[i]!=X and pos[i]!=O:
            pos[i] = player
            if if_Won(player):
                pos[i]=i+1
                return i+1
            else:
                pos[i]=i+1
    for i in range (9):
        if pos[i] != X and pos[i] != O:
            pos[i] = player2
            if if_Won(player2):
                pos[i]=i+1
                return i+1
            else:
                pos[i] = i+1
    #srodek wolny
    if pos[4] != X and pos[4] != O:
        return 5
    
    #srodek zajety 4 rogi wolne
    if (pos[4] == X or pos[4] == O) and (pos[0] != X and pos[0]!=O and pos[2]!=X and pos[2]!=O and pos[6]!=X and pos[6]!=O and pos[8]!=X and pos[8]!=O) and turn == 2:
        return random.choice([1,3,7,9])
    
    if Choice == '2' and turn == 4:
        #srodek i ukos vs ukos - not loosing
        if pos[4] == player2 and pos[0] == player2 and pos[8] == player:
            return random.choice([3,7])
        if pos[4] == player2 and pos[2] == player2 and pos[6] == player:
            return random.choice([1,9])
        if pos[4] == player2 and pos[8] == player2 and pos[0] == player:
            return random.choice([3,7])
        if pos[4] == player2 and pos[6] == player2 and pos[2] == player:
            return random.choice([1,9])
        
        #ukos i ukos vs srodek - not loosing
        if pos[4]==player and pos[0] == player2 and pos[8] == player2:
            return random.choice([2,4,6,8])
        if pos[4]==player and pos[2] == player2 and pos[6] == player2:
            return random.choice([2,4,6,8])
    if Choice == '3' and turn == 3:
        #winning by center - good def , second move  
        if pos[4] == player and pos[0] == player2:
            return 9
        if pos[4] == player and pos[2] == player2:
            return 7
        if pos[4] == player and pos[6] == player2:
            return 3
        if pos[4] == player and pos[8] == player2:
            return 1
        #winning by center - bad def, second move
    if Choice == '3' and  turn == 3:
        if pos[4] == player and pos[1] == player2:
            return 9
        if pos[4] == player and pos[3] == player2:
            return 3
        if pos[4] == player and pos[5] == player2:
            return 1
        if pos[4] == player and pos[7] == player2:
            return 1
    

    while True:
        random_move=random.randint(1,9)
        if pos[random_move-1] == X or pos[random_move-1] == O:
            continue
        else:
            return random_move

def if_Draw():
    for i in range(9):
        if (pos[i] != X and pos[i] != O):
            return False
    return True

def repair_board():
    global turn
    turn = 0
    for i in range(9):
        pos[i] = str(i+1)
X = 'X'
O = 'O'
turn = 0
If_Play = True
while (If_Play == True):
    pos = ['1','2','3','4','5','6','7','8','9']
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
            if (pos[tempX-1] != X and pos[tempX-1] != O):
                pos[tempX-1] = X
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
                        if tempY > 0 and tempY < 10:
                            Pole_Zajete_O = True
                            Input_Done = True
                        else:
                            print("Wybierz pole z mozliwego zakresu")
                    except Exception:
                        print("Robisz cos nie tak, sprobuj jeszcze raz!")
                else:
                    tempY=make_move(O)
                    random_correct_O = False
                    Pole_Zajete_O = True
                    Input_Done = True

            Input_Done = False

        while (Pole_Zajete_O == True):
            Pole_Zajete_O = False
            if (pos[tempY-1] != X and pos[tempY-1] != O):
                pos[tempY-1] = O
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
