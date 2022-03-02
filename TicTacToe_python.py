import os

clear = lambda: os.system("cls")
clear()

b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
char = ' '
line = "-----------"
s1 = " 1 | 2 | 3 "
s2 = "-----------"
s3 = " 4 | 5 | 6 "
s4 = "-----------"
s5 = " 7 | 8 | 9 "


def initialise_board():
    global s1
    global s2
    global s3
    global s4
    global s5
    global b

    s1 = "   |   |   "
    s2 = "-----------"
    s3 = "   |   |   "
    s4 = "-----------"
    s5 = "   |   |   "
    b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display(index, ch):
    global s1
    global s2
    global s3
    global s4
    global s5

    if index == 1: s1 = replacer(1, ch, s1)
    if index == 2: s1 = replacer(5, ch, s1)
    if index == 3: s1 = replacer(9, ch, s1)
    if index == 4: s3 = replacer(1, ch, s3)
    if index == 5: s3 = replacer(5, ch, s3)
    if index == 6: s3 = replacer(9, ch, s3)
    if index == 7: s5 = replacer(1, ch, s5)
    if index == 8: s5 = replacer(5, ch, s5)
    if index == 9: s5 = replacer(9, ch, s5)
    else: pass

    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)


def user_input():
    #i = input("What do you want to chose X or O \n")
    #j = 'O' if i == 'X' else 'X'
    ch = 'Y'

    while ch == 'Y':
        display(0, ' ')
        initialise_board()
        #display(0, ' ')
        c = 0
        count = 0
        ind = []
        for n in range(0, 9):
            if count >= 1:
                clear()
                display(0, ' ')
            else:
                pass
            if c == 0:
                index = int(input("Where do you want to input X: "))
                if index in ind:
                    print("Can't have 2 symbols at one place")
                    break
                else:
                    ind.append(index)
                display(index, 'X')
                b[index - 1] = 'X'
                if check_result('X') == 1:
                    print("X has won the game")
                    break
                else:
                    pass
                c += 1
            elif c == 1:
                index = int(input("Where do you want to input O: "))
                if index in ind:
                    print("Can't have 2 symbols at one place")
                    break
                else:
                    ind.append(index)
                display(index, 'O')
                b[index - 1] = 'O'
                if check_result('O') == 1:
                    print("O has won the game")
                    break
                else:
                    pass
                c -= 1
            count += 1
        else:
            print("Tie")
        ch = input("Do you want to play the game again press Y/N: ")
        initialise_board()
        clear()


def check_result(ch):
    if ((b[0] == b[1] == b[2] == ch) or (b[3] == b[4] == b[5] == ch)
            or (b[6] == b[7] == b[8] == ch) or (b[0] == b[4] == b[8] == ch)
            or (b[6] == b[4] == b[2] == ch) or (b[0] == b[3] == b[6] == ch)
            or (b[1] == b[4] == b[7] == ch) or (b[2] == b[5] == b[8] == ch)):
        return 1
    else:
        return 0


def replacer(ind, ch, line):
    return line[:ind] + ch + line[ind + 1:]


user_input()
