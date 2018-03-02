import random
import os

#To check wheather game is over or won .

def prove_no_possible_merges(a):
    for i in a:
        if(2048 in i):
            return 2

    for i in a:
        if(0 in i):
            return 1

    for i in a:
        for k in range(len(i)-1):
            if(i[k]==i[k+1]):
                return 1
    return 0


#moves

def check_move(a,move):
    if(move=='a' or move=='A' or move=='w' or move=='W' or move=='s' or move=='S' or move=='d' or move=='D'):
        return
    else:
        print("Invalid move Enter again :")
        move=input()
        check_move(a,move)
    pass


def shift(a):
    temp=[0]*len(a)
    for i in a:
        if(i!=0):
            temp.append(i)
    a=temp

def make_order(board):
    for i in board:
        shift(i)


def merge(board):

    for i in board:
        for k in range(len(i)-1):
            if(i[k]==i[k+1]):
                i[k]=i[k]+i[k+1]
                i[k+1]=0
                k=k+1
    make_order(board)
    pass


#print board
def print_board(board):
    for i in board:
        for k in i:
            print(k,end=' ')
        print('')






name=input()
print("Enter the board size (4,5,6) : ")
size=int(input())
board=[]
rand=[2,2,2,4,2,2,2,2,4,2,2,2,4,2,2]
for i in range(size):
    board.append([0]*size)




x=prove_no_possible_merges(board)
while(x):
    if(x==2):
        break

    val=rand[random.randint(0,len(rand)-1)]
    pos1=random.randint(0,len(board)-1)
    pos2=random.randint(0,len(board)-1)

    if(board[pos1][pos2]==0):
        board[pos1][pos2]=val
    else:
        continue

    print("Enter your move (w for up , d for right , a for left , s for down ) :")
    move=input()

    check_move(board,move)

    if(move== 'a' or move == 'A'):
        merge(board)


    if (move == 'd' or move == 'D'):
        for i in board:
            i.reverse()

        merge(board)

        for i in board:
            i.reverse()

    if(move=='s' or move == "S"):
        board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

        for i in board:
            i.reverse()

        merge(board)

        for i in board:
            i.reverse()

        board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

        pass

    if(move=='W' or move == "w"):

        board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

        merge(board)

        board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

        pass



    print_board(board)

    x=prove_no_possible_merges(board)

if(x==2):
    print("You won")
else :
    print("You lost")



