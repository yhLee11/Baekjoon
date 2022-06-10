import sys
input=sys.stdin.readline
sudoku=[list(map(int,input().split())) for _ in range(9)]
zero=[]
loc={0:[0,1,2],3:[3,4,5],6:[6,7,8]}
def isNotInCol(num,y):
    for i in range(9):
        if sudoku[i][y]==num:
            return False
    return True

def isNotIn3by3(num,x,y):
    #어느 구역에 있는지 확인 필요
    sx,sy=-1,-1
    for k,v in loc.items():
        if x in v:
            sx=k
        if y in v:
            sy=k
    for i in range(sx,sx+3):
        for j in range(sy,sy+3):
            if num==sudoku[i][j]:
                return False
    return True

def dfs(idx):
    if idx==len(zero):
        for s in sudoku:
            print(' '.join(map(str,s)))
        exit(0)

    for num in range(1,10):
        x=zero[idx][0]
        y=zero[idx][1]
        if num not in sudoku[x] and isNotInCol(num,y) and isNotIn3by3(num,x,y):
            sudoku[x][y]=num
            dfs(idx+1)
            sudoku[x][y]=0

for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            zero.append((i,j))

dfs(0)