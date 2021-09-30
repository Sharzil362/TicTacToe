##GAME_OF_TicTacToe##
#board      #0/0      #2/2     #4/4
org_table=[['-',' | ','-',' | ','-'],
            #5/0     #7/2      #9/4
           ['-',' | ','-',' | ','-'],
            #10/0    #12/2     #14/4
           ['-',' | ','-',' | ','-']]
def table():
    global org_table
    for count in org_table:
        for i in count:
            print(i,end='')
        print()
def game():
    global org_table
    #userX
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
    #userY
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
def winner():
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
            print('''X wins.''')
            return 'Game Over'
        elif O==3:
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
            print('X wins')
            return 'Game Over'
        elif row_O==3:
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
            print('X Wins')
            return 'Game Over'
        elif row_O==3:
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
            print('X Wins')
            return 'Game Over'
        elif row_O==3:
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
        print('X Wins')
        return 'Game Over'
    if diagonal_o_left==3:
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
        print('X Wins')
        return 'Game Over'
    if diagonal_o_right==3:
        print('O wins')
        return 'Game Over'
    return ''
