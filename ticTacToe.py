import itertools
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

#horizontally winner
for row in game:
    #print(row)
    if row.count(row[0]) == len(row) and row[0] != 0:
        print(f"Player {row[0]} is horizontally winner")

#vertically winner
for col in range(len(game[0])):
    check = []
    for row in game:
        check.append(row[col])
    if check.count(check[0]) == len(check) and check[0] != 0:
        print(f"Player {check[0]} is vertically winner")

# \ diagonally winner
diag = []
for cross in range(len(game)):
    diag.append(game[cross][cross])
if diag.count(diag[0]) == len(diag) and diag[0] != 0:
    print(f"Player {diag[0]} is diagonally winner \\")

# / diagonnaly winner
diag = []
for idx, rev_idx in enumerate(reversed(range(len(game)))):
    diag.append(game[idx][rev_idx]) 

if diag.count(diag[0]) == len(diag) and diag[0] != 0:
    print(f"Player {diag[0]} is diagonally winner /")

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return False

play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    player_cycle = itertools.cycle(players)
    game_board(game,just_display = True)
    while not game_won:
        current_player = next(player_cycle)
        print(f"Player: {current_player}")
        column_choice = int(input("Which column? "))
        row_choice = int(input("Which row? "))

        game_board(game, player = current_player, row=row_choice, column=column_choice)