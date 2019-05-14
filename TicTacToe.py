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
    system('clear')
    print("                                  _" +
          pos[0]+"_|"+"_"+pos[1]+"_|"+"_"+pos[2]+"_")
    print("                                  _" +
          pos[3]+"_|"+"_"+pos[4]+"_|"+"_"+pos[5]+"_")
    print("                                  _" +
          pos[6]+"_|"+"_"+pos[7]+"_|"+"_"+pos[8]+"_")
# ---------------------------------------------------------------------------------------------------


def if_Won():
    # winners = [
    #     (0, 1, 2),
    #     (3, 4, 5),
    #     (6, 7, 8),
    #     (0, 3, 6),
    #     (1, 4, 7),
    #     (2, 5, 8),
    #     (0, 4, 8),
    #     (2, 4, 6),
    # ]

    if(pos[0] == pos[1] and pos[1] == pos[2]):
        return True
    elif(pos[3] == pos[4] and pos[4] == pos[5]):
        return True
    elif(pos[6] == pos[7] and pos[7] == pos[8]):
        return True
    elif(pos[0] == pos[3] and pos[3] == pos[6]):
        return True
    elif(pos[1] == pos[4] and pos[4] == pos[7]):
        return True
    elif(pos[2] == pos[5] and pos[5] == pos[8]):
        return True
    elif(pos[0] == pos[4] and pos[4] == pos[8]):
        return True
    elif(pos[2] == pos[4] and pos[4] == pos[6]):
        return True

    return False
# ---------------------------------------------------------------------


def if_Draw():
    for i in range(9):
        if (pos[i] != 'X' and pos[i] != 'O'):
            return False
    return True

def repair_board():
    for i in range(9):
        pos[i] = str(i+1)

If_Play = True
while (If_Play == True):
    pos = ['1','2','3','4','5','6','7','8','9']
    random_correct_X = False
    random_correct_O = False
    Input_Done = False
    Choice = print_menu()
    print_board()
    while(not if_Won()):
        while (Input_Done == False):

            if(Choice == '1' or Choice == '2'):
                try:
                    tempX = int(input("Wybierz pole(X):"))
                    Pole_Zajete_X = True
                    Input_Done = True
                except:
                    print("Robisz cos nie tak, sprobuj jeszcze raz!")
            else:
                while(random_correct_X == False):
                    tempX = random.randint(0, 9)
                    if(pos[tempX-1] != 'X' and pos[tempX-1] != 'O'):
                        random_correct_X = True
                random_correct_X = False
                Pole_Zajete_X = True
                Input_Done = True
        Input_Done = False

        while (Pole_Zajete_X == True):
            Pole_Zajete_X = False
            if (pos[tempX-1] != "X" and pos[tempX-1] != "O"):
                pos[tempX-1] = "X"
                print_board()
                if(if_Won()):
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
        if(if_Draw()):
            print("Brak mozliwosci dalszych ruchow, REMIS")
            Pole_Zajete_X = False
            break
        if(not if_Won() and not if_Draw()):
            while(Input_Done == False):
                if(Choice == '1' or Choice == '3'):
                    try:
                        tempY = int(input("Wybierz pole(O):"))
                        Pole_Zajete_O = True
                        Input_Done = True
                    except:
                        print("Robisz cos nie tak, sprobuj jeszcze raz!")
                else:
                    while(random_correct_O == False):
                        tempY = random.randint(0, 9)
                        if(pos[tempY-1] != 'X' and pos[tempY-1] != 'O'):
                            random_correct_O = True
                    random_correct_O = False
                    Pole_Zajete_O = True
                Input_Done = True

            Input_Done = False

        while (Pole_Zajete_O == True):
            Pole_Zajete_O = False
            if (pos[tempY-1] != "X" and pos[tempY-1] != "O"):
                pos[tempY-1] = "O"
                print_board()
                if(if_Won()):
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
                    except:
                        print("Robisz cos nie tak, sprobuj jeszcze raz!")
                Input_Done = False
    if (input("Jesli chcesz grac dalej wpisz 'tak' i wcisnij enter, aby zakonczyc cokolwiek innego:") == 'tak'):
        repair_board()
        print_board()
    else:
        If_Play=False
