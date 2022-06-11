import sys
from collections import deque
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]
R,C=map(int,input().split())
board=[list(input().strip()) for _ in range(R)]
visit=[[False]*C for _ in range(R)]
sonic=deque()
water=deque()
cnt=0
def bfs(sonic,water):
    global cnt
    while sonic:#sonic이 이동할 칸이 있는 경우
        for _ in range(len(water)):
            wx,wy=water.popleft()
            for i in range(4):
                nx=wx+dx[i]
                ny=wy+dy[i]
                if 0<=nx<R and 0<=ny<C and board[nx][ny]=='.':
                    board[nx][ny]='*'
                    visit[nx][ny]=True
                    water.append((nx,ny))
        cnt+=1
        for _ in range(len(sonic)):
            sx,sy=sonic.popleft()
            for i in range(4):
                nx=sx+dx[i]
                ny=sy+dy[i]
                if 0<=nx<R and 0<=ny<C and not visit[nx][ny]:
                    if board[nx][ny]=='.':
                        visit[nx][ny]=True
                        sonic.append((nx,ny))
                    elif board[nx][ny]=='D':
                        return print(cnt)
                        
    return print("KAKTUS")

for i in range(R):
    for j in range(C):
        if board[i][j]=='S':
            sonic.append((i,j))
            visit[i][j]=True
        elif board[i][j]=='*':
            water.append((i,j))
            visit[i][j]=True
        elif board[i][j]=='X':
            visit[i][j]=True

bfs(sonic,water)