row = 0
columns = 0
table = ['1','2','3'], ['4','5','6'], ['7','8','9']
running = True

def print_grid():
    for row in range(len(table)):
        for column in range(len(table[row])):
            if column == 2:
                print(" " + table[row][column], end="")
            else:
                print(" " + table[row][column] + " " , end= "|")
        print()
        print(end='-----------')
        print()

def update_grid(pl, pi):
    for row in range(len(table)):
        for column in range(len(table[row])):
            if pl == table[row][column] and (pi == 'x' or pi=='o'):
                table[row][column] = pi
                break

for i in range(9):
    player1 = input()
    piece1 = input()
    update_grid(player1, piece1)
    print_grid()