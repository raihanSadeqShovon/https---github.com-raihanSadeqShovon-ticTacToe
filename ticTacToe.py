import itertools

def win(current_game):

    def all_same(p):
        if p.count(p[0]) == len(p) and p[0] != 0:
            return True
        else:
            return False

    #horizontally winner
    for row in game:
        #print(row)
        if all_same(row):
            print(f"Player {row[0]} is horizontally winner")
            return True

    #vertically winner
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is vertically winner")
            return True

    # \ diagonally winner
    diag = []
    for cross in range(len(game)):
        diag.append(game[cross][cross])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print(f"Player {diag[0]} is diagonally winner \\")
        return True

    # / diagonnaly winner
    diag = []
    for idx, rev_idx in enumerate(reversed(range(len(game)))):
        diag.append(game[idx][rev_idx]) 

    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print(f"Player {diag[0]} is diagonally winner /")
        return True
    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied! Choose another!")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player

        for count, row in enumerate(game_map):
            print(count, row)

        return game_map, True

    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)")
        return game_map, False

    except Exception as e:
        print(str(e))
        return game_map, False

play = True
players = [1, 2]
while play:

    game_size = int(input("What is the size of your game? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game,just_display = True) 
    player_cycle = itertools.cycle(players)
    
    while not game_won:
        current_player = next(player_cycle)
        print(f"Player: {current_player}")
        played = False
        while not played:
            column_choice = int(input("Which column do you want to play? (0, 1, 2): "))
            row_choice = int(input("Which row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)
        
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Byeeee")
                play = False
            else:
                print("Not a valid answer, see you later alegator")
                play = False