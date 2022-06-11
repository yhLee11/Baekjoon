import sys,copy
input=sys.stdin.readline
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
ans=0
def move(d,board):
    if d==0:#동
        for i in range(n):
            top=n-1
            for j in range(n-2,-1,-1):#n-2~0
                if board[i][j]:#0이 아니면
                    tmp=board[i][j]
                    board[i][j]=0
                    if board[i][top]==0:
                        board[i][top]=tmp
                    elif board[i][top]==tmp:
                        board[i][top]=2*tmp
                        top-=1
                    else:
                        top-=1
                        board[i][top]=tmp
    elif d==1:#서
        for i in range(n):
            top=0
            for j in range(1,n):
                if board[i][j]:
                    tmp=board[i][j]
                    board[i][j]=0
                    if board[i][top]==0:
                        board[i][top]=tmp
                    elif board[i][top]==tmp:
                        board[i][top]=2*tmp
                        top+=1
                    else:
                        top+=1
                        board[i][top]=tmp
    elif d==2:#남
        for j in range(n):
            top=n-1
            for i in range(n-2,-1,-1):
                if board[i][j]:
                    tmp=board[i][j]
                    board[i][j]=0
                    if board[top][j]==0:
                        board[top][j]=tmp
                    elif board[top][j]==tmp:
                        board[top][j]=2*tmp
                        top-=1
                    else:
                        top-=1
                        board[top][j]=tmp
    elif d==3:#북
        for j in range(n):
            top=0
            for i in range(1,n):
                if board[i][j]:
                    tmp=board[i][j]
                    board[i][j]=0
                    if board[top][j]==0:
                        board[top][j]=tmp
                    elif board[top][j]==tmp:
                        board[top][j]=2*tmp
                        top+=1
                    else:
                        top+=1
                        board[top][j]=tmp

    return board
def dfs(board,cnt):
    global ans
    if cnt==5:
        for i in range(n):
            for j in range(n):
                ans=max(ans,board[i][j])
        return
    for i in range(4):
        nboard=move(i,copy.deepcopy(board))
        dfs(nboard,cnt+1)
dfs(board,0)
print(ans)
    