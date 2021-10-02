##GAME_OF_TicTacToe##
#board      #0        #2        #4
org_table=[['-',' | ','-',' | ','-'],
            #0        #2        #4
           ['-',' | ','-',' | ','-'],
            #0         #2       #4
           ['-',' | ','-',' | ','-']]

# for breaking the while loop
break_it = 0
def table():
    global org_table
    for count in org_table:
        for i in count:
            print(i,end='')
        print()

def game():
    global org_table
    #userX
    print("X's Turn: ")
    try:
        user_input=int(input())
        if user_input>9 or user_input<=0:
            print('such place does not exist')
            raise ValueError
        else:
            if user_input==1 and org_table[0][0]!='O':
                org_table[0][0]='X'
            elif user_input==2 and org_table[0][2]!='O':
                org_table[0][2]='X'
            elif user_input==3 and org_table[0][4]!='O':
                org_table[0][4]='X'
            elif user_input==4 and org_table[1][0]!='O':
                org_table[1][0]='X'
            elif user_input==5 and org_table[1][2]!='O':
                org_table[1][2]='X'
            elif user_input==6 and org_table[1][4]!='O':
                org_table[1][4]='X'
            elif user_input==7 and org_table[2][0]!='O':
                org_table[2][0]='X'
            elif user_input==8 and org_table[2][2]!='O':
                org_table[2][2]='X'
            elif user_input==9 and org_table[2][4]!='O':
                org_table[2][4]='X'
            print(winner())
            table()
            if break_it > 0:
                return ''
    except ValueError:
        print('''Try Again, this time try in the Range 1-9''')
        user_input=int(input())
        if user_input == 1 and org_table[0][0] != 'O':
            org_table[0][0] = 'X'
        elif user_input == 2 and org_table[0][2] != 'O':
            org_table[0][2] = 'X'
        elif user_input == 3 and org_table[0][4] != 'O':
            org_table[0][4] = 'X'
        elif user_input == 4 and org_table[1][0] != 'O':
            org_table[1][0] = 'X'
        elif user_input == 5 and org_table[1][2] != 'O':
            org_table[1][2] = 'X'
        elif user_input == 6 and org_table[1][4] != 'O':
            org_table[1][4] = 'X'
        elif user_input == 7 and org_table[2][0] != 'O':
            org_table[2][0] = 'X'
        elif user_input == 8 and org_table[2][2] != 'O':
            org_table[2][2] = 'X'
        elif user_input == 9 and org_table[2][4] != 'O':
            org_table[2][4] = 'X'
        print(winner())
        table()
        if break_it>0:
            return ''
    #userY
    print("O's Turn: ")
    try:
        user_input=int(input())
        if user_input>9 or user_input<=0:
            print('such place does not exist')
            raise ValueError
        else:
            if user_input==1 and org_table[0][0]!='X':
                org_table[0][0]='O'
            elif user_input==2 and org_table[0][2]!='X':
                org_table[0][2]='O'
            elif user_input==3 and org_table[0][4]!='X':
                org_table[0][4]='O'
            elif user_input==4 and org_table[1][0]!='X':
                org_table[1][0]='O'
            elif user_input==5 and org_table[1][2]!='X':
                org_table[1][2]='O'
            elif user_input==6 and org_table[1][4]!='X':
                org_table[1][4]='O'
            elif user_input==7 and org_table[2][0]!='X':
                org_table[2][0]='O'
            elif user_input==8 and org_table[2][2]!='X':
                org_table[2][2]='O'
            elif user_input==9 and org_table[2][4]!='X':
                org_table[2][4]='O'
            print(winner())
            table()
            if break_it>0:
                return ''
    except ValueError:
        print('''Try Again, this time try in the Range 1-9''')
        user_input=int(input())
        if user_input == 1 and org_table[0][0] != 'X':
            org_table[0][0] = 'O'
        elif user_input == 2 and org_table[0][2] != 'X':
            org_table[0][2] = 'O'
        elif user_input == 3 and org_table[0][4] != 'X':
            org_table[0][4] = 'O'
        elif user_input == 4 and org_table[1][0] != 'X':
            org_table[1][0] = 'O'
        elif user_input == 5 and org_table[1][2] != 'X':
            org_table[1][2] = 'O'
        elif user_input == 6 and org_table[2][4] != 'X':
            org_table[2][4] = 'O'
        elif user_input == 7 and org_table[2][0] != 'X':
            org_table[2][0] = 'O'
        elif user_input == 8 and org_table[2][2] != 'X':
            org_table[2][2] = 'O'
        elif user_input == 9 and org_table[2][4] != 'X':
            org_table[2][4] = 'O'
        print(winner())
        table()
        if break_it>0:
            return ''
def winner():
    global break_it
    #coloumn_checker
    for count in org_table:
        X=0
        O=0
        for i in count:
            if i=='X':
                X+=1
            elif i=='O':
                O+=1
        if X==3 and O==3:
            print('''It is a draw.''')
            return 'Game Over'
        elif X==3:
            break_it+=1
            print('''X wins.''')
            return 'Game Over'
        elif O==3:
            break_it += 1
            print('''O wins.''')
            return 'Game Over'
        X=0
        O=0
    #Row_Checker
    row_X = 0
    row_O = 0
    for count in org_table:
        # Row_One
        if count[0]=='X':
            row_X+=1
        elif count[0]=='O':
            row_O+=1
        if row_X==3:
            break_it += 1
            print('X wins')
            return 'Game Over'
        elif row_O==3:
            break_it += 1
            print('O Wins')
            return 'Game Over'
    row_O=0
    row_X=0
        #Row_Two
    for count in org_table:
        if count[1]=='X':
            row_X+=1
        elif count[1]=='O':
            row_O+=1
        if row_X==3:
            break_it += 1
            print('X Wins')
            return 'Game Over'
        elif row_O==3:
            break_it += 1
            print('O Wins')
            return 'Game Over'
    row_O=0
    row_X=0
        #Row_Three
    for count in org_table:
        if count[4]=='X':
            row_X+=1
        elif count[4]=='O':
            row_O+=1
        if row_X==3:
            break_it += 1
            print('X Wins')
            return 'Game Over'
        elif row_O==3:
            break_it += 1
            print('O Wins')
            return 'Game Over'
    ##Diagonal_Checker##
    diagonal_x_left = 0
    diagonal_o_left = 0
    diagonal_x_right=0
    diagonal_o_right=0
    #left to right
    if org_table[0][0]=='X':
        diagonal_x_left+=1
    elif org_table[0][0]=='O':
        diagonal_o_left+=1
    if org_table[1][2]=='X':
        diagonal_x_left+=1
    elif org_table[1][2]=='O':
        diagonal_o_left+=1
    if org_table[2][4]=='X':
        diagonal_x_left+=1
    elif org_table[2][4]=='O':
        diagonal_o_left+=1
    if diagonal_x_left==3:
        break_it += 1
        print('X Wins')
        return 'Game Over'
    if diagonal_o_left==3:
        break_it += 1
        print('O wins')
        return 'Game Over'
    #right to left
    if org_table[0][4]=='X':
        diagonal_x_right+=1
    elif org_table[0][4]=='O':
        diagonal_o_right+=1
    if org_table[1][2]=='X':
        diagonal_x_right+=1
    elif org_table[1][2]=='O':
        diagonal_o_right+=1
    if org_table[2][0]=='X':
        diagonal_x_right+=1
    elif org_table[2][0]=='O':
        diagonal_o_right+=1
    if diagonal_x_right==3:
        break_it += 1
        print('X Wins')
        return 'Game Over'
    if diagonal_o_right==3:
        break_it += 1
        print('O wins')
        return 'Game Over'
    return ''


try:
    print('To start the Game type the Keyword "start" and press enter to start the game')
    user_input = input('Enter The Keyword:  ')
    if user_input == 'start':
        print('''The rules of the game are simple and as follows:
------------------------------------------------    
1. The game is played on a grid that's 3 squares by 3 squares.
2. You(first person) are "X", your friend (second person) is "O". Players take turns putting their marks in empty squares.
3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
4. You must enter a value in the range of 1-9
5. Each square is numbered according to the convention below:
                    1 | 2 | 3
                    4 | 5 | 6
                    7 | 8 | 9
----------------------------------------------------------------------------------------------------
 _____                  
|         /\   |\  /|  |----
|  ___   /  \  | \/ |  |----
|__| |  /    \ |    |  |----
     ______________
        \      / 
         \    /
        __\  /__
        \      /
         \    /
          \  /
           \/
           
        - | - | -
        - | - | -
        - | - | -
      ''')
        while True:
            if break_it == 0:
                game()
            else:
                break
    elif user_input != 'start':
        raise ValueError
except ValueError:
    print('please type the keyword "start" and press enter to begin')
    user_input = input('Enter The Keyword:  ')
    if user_input == 'start':
        print('''The rules of the game are simple and as follows:
    ------------------------------------------------    
    1. The game is played on a grid that's 3 squares by 3 squares.
    2. You(first person) are "X", your friend (second person) is "O". Players take turns putting their marks in empty squares.
    3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
    4. You must enter a value in the range of 1-9
    5. Each square is numbered according to the convention below:
                        1 | 2 | 3
                        4 | 5 | 6
                        7 | 8 | 9
    ----------------------------------------------------------------------------------------------------
     _____                  
    |         /\   |\  /|  |----
    |  ___   /  \  | \/ |  |----
    |__| |  /    \ |    |  |----
         ______________
            \      / 
             \    /
            __\  /__
            \      /
             \    /
              \  /
               \/

            - | - | -
            - | - | -
            - | - | -
          ''')
        while True:
            if break_it == 0:
                game()
            else:
                break





