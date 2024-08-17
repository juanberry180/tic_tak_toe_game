Player_A = "O"
Player_B = "X"

scores = {1:{1:0, 2:0, 3:0}, 2:{1:0, 2:0, 3:0}, 3:{1:0, 2:0, 3:0}}

def show_table():
    for row in range(len(scores)):
        output = ''
        for column in scores[row+1]:
            if column < 3:
                if scores[row+1][column] == 1:
                    output += ' O |'
                elif scores[row+1][column] == 5:
                    output += ' X |'
                else:
                    output += '  |'
            else:
                if scores[row+1][column] == 1:
                    output += ' O '
                elif scores[row+1][column] == 5:
                    output += ' X '
                else:
                    output += '  '
        print(output)
        if row < 2:
            print("---------")

def playingA():
    rowA = int(input(f'Player A  - {Player_A}, please indicate in which row you want to put your sign from 1 to 3?'))
    colA = int(input(f'Please A - {Player_A}, please indicate in which column you want to put your sign from 1 to 3?'))
    if rowA > 3 or rowA < 1 or colA > 3 or colA < 1:
        print('Numbers are out of range, please try again.')
        playingA()
    else:
        if scores[rowA][colA] != 0:
            print("This place is already taken, please choose another place.")
            playingA()
        scores[int(rowA)][int(colA)] = 1
        return scores

def playingB():
    rowB = int(input(f'Player B  - {Player_B}, please indicate in which row you want to put your sign from 1 to 3?'))
    colB = int(input(f'Please B - {Player_B}, please indicate in which column you want to put your sign from 1 to 3?'))
    if rowB > 3 or rowB < 1 or colB > 3 or colB < 1:
        print('Numbers are out of range, please try again.')
        playingA()
    if scores[rowB][colB] != 0:
        print("This place is already taken, please choose another place")
        playingB()
    scores[int(rowB)][int(colB)] = 5
    return scores


def scores_calculating():
    suma_horizontal = {1: 0, 2: 0, 3: 0}
    suma_vertical = {1: 0, 2: 0, 3: 0}
    suma_diagonal = {1: 0, 2: 0}
    for row in range(len(scores)):
        suma_horizontal[row + 1] = sum(scores[row + 1].values())
        for col in range(len(scores[row+1])):
            suma_vertical[col+1] += scores[row+1][col+1]
    suma_diagonal[1] = scores[1][1]+scores[2][2]+scores[3][3]
    suma_diagonal[2] = scores[1][3]+scores[2][2]+scores[3][1]
    for row in suma_horizontal:
        if suma_horizontal[row] == 3:
            print('PlayerA Win!')
            game_on = False
            return game_on
        elif suma_horizontal[row] == 15:
            print('PlayerB Win!')
            game_on = False
            return game_on
        else:
            game_on = True
            return game_on
    for column in suma_vertical:
        if suma_vertical[column] == 3:
            print('PlayerA Win!')
            game_on = False
            return game_on
        elif suma_vertical[column] == 15:
            print('PlayerB Win!')
            game_on = False
            return game_on
        else:
            game_on = True
            return game_on

    for diagonal in suma_diagonal:
        if suma_diagonal[diagonal] == 3:
            print('PlayerA Win!')
            game_on = False
            return game_on
        elif suma_diagonal[diagonal] == 15:
            print('PlayerB Win!')
            game_on = False
            return game_on
        else:
            game_on = True
            return game_on




game_on  = True
while game_on:
    playingA()
    show_table()
    game_on = scores_calculating()
    if game_on:
        playingB()
        show_table()
        game_on = scores_calculating()

















