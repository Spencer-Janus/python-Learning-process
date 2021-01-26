BOARD_SIZE=15
#定义一个二位列表来表示棋盘
board=[]
def initboard():
    for i in range(BOARD_SIZE):
        row=['+']*BOARD_SIZE
        board.append(row)
def printboard():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j],end='')
        print('')
initboard()
printboard()
