import random
TicTacToe =  [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]



def game_won(player_A, player_B):
    count_A = 0
    count_B = 0 
    for j in TicTacToe:
        for i in j:
            if i == player_A:
                count_A+= 1
                count_B = 0
            elif i == player_B:
                count_B+= 1
                count_A = 0
            else: count_A = count_B = 0
            if count_A == 3 or count_B == 3:
                print('1')
                print(f"{player_A if count_A ==3 else player_B} wins!")
                return True
    print("part_1")
    count_B = 0
    count_A = 0
    for m in range(len(TicTacToe)):
        for p in range(len(TicTacToe[m])):
            if TicTacToe[p][m] == player_A:
                count_A+= 1
                count_B = 0
            elif TicTacToe[p][m] == player_B:
                count_B+= 1
                count_A = 0
            else: 
                    count_A = 0
                    count_B = 0
            if count_A == 3 or count_B == 3:
                print('2')
                print(f"{player_A if count_A ==3 else player_B} wins!")
                return True

    print("part_2")
    if TicTacToe[0][0] == player_A and TicTacToe[1][1] == player_A and TicTacToe[2][2] == player_A:
        print(player_A + " has won part1")
        return True
    elif TicTacToe[0][0] == player_B and TicTacToe[1][1] == player_B and TicTacToe[2][2] == player_B:
        print(player_B + " has won part2")
        return True
    elif TicTacToe[0][2] ==player_A and TicTacToe[1][1] == player_A and TicTacToe[2][0] == player_A:
        print(player_A + " has won part3")
        return True
    elif TicTacToe[0][2] == player_B and TicTacToe[1][1] == player_B and TicTacToe[2][0] == player_B:
        print(player_B + " has won part4")
        return True



print("Welcome to a game of Tic Tac Toe")
player1 =  'X'
player2 = 'O'

for i in range(0,9):
        print("Player 1 choose a square, enter the row and column")
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        while True : 
            if TicTacToe[int(row)][int(column)] != '':
                print("Please try agin as sqaure is already taken")
                print("enter the row and column:")
                row = random.randint(0, 2)
                column = random.randint(0, 2)
            else:
                TicTacToe[int(row)][int(column)] = player1
                break
        for z in range(len(TicTacToe)):
            print(TicTacToe[z])
        if game_won(player1,player2) == True:
            for z in range(len(TicTacToe)):
                print(TicTacToe[z])
            print("Game is over")
            break

        print("Player 2 choose a square, enter the row and column")
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        while True: 
            if TicTacToe[int(row)][int(column)] != '':
                print("Please try agin as sqaure is already taken")
                print("enter the row and column:")
                row = random.randint(0, 2)
                column = random.randint(0, 2)
            else: 
                TicTacToe[int(row)][int(column)] = player2
                break
        for z in range(len(TicTacToe)):
            print(TicTacToe[z])
        if game_won(player1,player2) == True:
            for z in range(len(TicTacToe)):
                print(TicTacToe[z])
            print("Game is over")
            break





