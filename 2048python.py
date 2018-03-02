import random
import os

def proved_no_possible_merges(a):
    if(a.find(0)):
        return 1
    if(a.fin(2048)):
        return 2
    for i in a:
        for k in range(len(i)-1):
            if(i[k]==i[k+1]):
                return 1
    return 0

name=input()
print("Enter the board size (4,5,6) : ")
size=int(input())
board=[]
for i in range(size):
    board.append([0]*size)


rand=[2,2,2,4,2,2,2,2,4,2,2,2,4,2,2]

x=proved_no_possible_merges(board)
while(x):
    os.system('CLS')
    val=rand[random.randint(0,len(rand)-1)]
    pos1=random.randint(0,len(board)-1)
    pos2=random.randint(0,len(board)-1)
    print(pos1,pos2)
    if(board[pos1][pos2]==0):
        board[pos1][pos2]=val
    else:
        continue
    for i in board:
        for k in i :
            print(k,end=' ')
        print('')
    x=proved_no_possible_merges(board)



