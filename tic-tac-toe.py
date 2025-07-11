players = [['',''],['','']]
players[0][0] = input("Enter player 01 name: ")
players[0][1] = input("Enter player 01 symbol: ")

players[1][0] = input("Enter player 02 name: ")
players[1][1] = input("Enter player 02 symbol: ")

winner = ''
blank = " "
coinposition = [[blank,blank,blank],[blank,blank,blank], [blank,blank,blank]]
placeposition = [[[1,2],[1,6],[1,10]],[[3,2],[3,6],[3,10]],[[5,2],[5,6],[5,10]]]
gameboard = [
             ['\u2554', '\u2550', '\u2550', '\u2550', '\u2566', '\u2550', '\u2550', '\u2550', '\u2566', '\u2550', '\u2550', '\u2550', '\u2557'],
             ['\u2551', blank, blank, blank, '\u2551', blank, blank, blank, '\u2551', blank, blank, blank, '\u2551'],
             ['\u2560', '\u2550', '\u2550', '\u2550', '\u256c', '\u2550', '\u2550', '\u2550', '\u256c', '\u2550', '\u2550', '\u2550', '\u2563'],
             ['\u2551', blank, blank, blank, '\u2551', blank, blank, blank, '\u2551',blank, blank, blank, '\u2551'],
             ['\u2560', '\u2550', '\u2550', '\u2550', '\u256c', '\u2550', '\u2550', '\u2550', '\u256c', '\u2550', '\u2550', '\u2550', '\u2563'],
             ['\u2551', blank, blank, blank, '\u2551', blank, blank, blank, '\u2551',blank, blank, blank, '\u2551'],
             ['\u255a', '\u2550', '\u2550', '\u2550', '\u2569', '\u2550', '\u2550', '\u2550', '\u2569', '\u2550', '\u2550', '\u2550', '\u255d']
            ]

# Display the game board
for row in gameboard:
    for item in row:
        print(item, end="")
    print()

for move in range(9):
    if move % 2 == 0:
        player = players[0][0]
        symbol = players[0][1]
    else:
        player = players[1][0]
        symbol = players[1][1]
    
    getinput = True
    while getinput:
        getinput = False
        print(f"{player}'s turn ({symbol})")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input, please enter row and column between 0 and 2.")
            getinput = True
            continue

        if coinposition[row][col] == blank:
            coinposition[row][col] = symbol
            place = placeposition[row][col]
            gameboard[place[0]][place[1]] = symbol
        else:
            print("Position already taken, try again.")
            getinput = True

    # Display the updated game board
    for r in gameboard:
        for item in r:
            print(item, end="")
        print()
    
    if move >= 4:  # Check for a winner after the 5th move
        # Check rows, columns, and diagonals for a winner   
        for i in range(3):
            if coinposition[i][0] == coinposition[i][1] == coinposition[i][2] != blank:                
                winner = coinposition[i][0]
                break
            if coinposition[0][i] == coinposition[1][i] == coinposition[2][i] != blank:
                winner = coinposition[0][i]

                break                        
        if not winner:
            if coinposition[0][0] == coinposition[1][1] == coinposition[2][2] != blank:
                winner = coinposition[0][0]
            elif coinposition[0][2] == coinposition[1][1] == coinposition[2][0] != blank:
                winner = coinposition[0][2]

        if len(winner)> 0:
            break

if len(winner)> 0:
    if move % 2 == 0:
        winner = players[0][0]
        symbol = players[0][1]
    else:
        winner = players[1][0]
        symbol = players[1][1]
    print(f"Congratulations {winner}({symbol}), you win!")
else:
    print("It's a draw!")
    

