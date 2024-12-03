row = 0
columns = 0
table = ['1','2','3'], ['4','5','6'], ['7','8','9']
running = True
count = 0
R = False
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

def update_grid():

    pl = input()
    pi = input()
    while int(pl)<=0 or int(pl) >=10:
        print("Whoops you tried to cheat, try again and do it right this time!")
        pl = input()
        pi = input()

    for row in range(len(table)):
        for column in range(len(table[row])):
            r = False
            if pl == pi and table[row][column] == pi and pl == table[row][column] and (pi == "x" or pi == "o"):
                table[row][column] = pi
            if pi == table[row][column] and (pi == "x" or pi == "o"):
                print("Whoops you tried to cheat, try again and do it right this time!")
                pl = input()
                pi = input()
                r = False
            while r == False and pi == table[row][column] and table[row][column] == pl:
                print("Whoops you tried to cheat, try again and do it right this time!")
                pl = input()
                pi = input()
            if pl == table[row][column] and (pi == 'x' or pi == 'o'):
                table[row][column] = pi
                break






def winning_c():
    for col in range(len(table)):
        if table[0][col] == table[1][col] == table[2][col]:
            print("Winner is " + table[0][col])
            return True
    for row in range(len(table)):
        if table[row][0] == table[row][1] == table[row][2]:
            print("Winner is " + table[row][0])
            return True

    if table[0][0] == table[1][1] == table[2][2]:
        print("Winner is " + table[0][0])
        return True

    elif table[0][2] == table[1][1] == table[2][0]:
        print("Winner is " + table[0][2])
        return True
    return False

print_grid()
for i in range(9):


    count+=1
    update_grid()
    print_grid()

    if winning_c() == False and count==9:
       print("Its a draw")

