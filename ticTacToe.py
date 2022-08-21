game = [[2,2,2],
        [1,2,3],
        [0,2,2]]
def tictactoe():
    #horizontally winner
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is horizontally winner")

    #vertically winner
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is vertically winner")

    #diagonally winner
    diag = []
    for cross in range(len(game)):
        diag.append(game[cross][cross])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print(f"Player {diag[0]} is diagonally winner")

tictactoe()