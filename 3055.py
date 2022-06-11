import sys
from collections import deque
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]
R,C=map(int,input().split())
board=[list(input().strip()) for _ in range(R)]
visit=[[False]*C for _ in range(R)]
sonic,water=deque(),deque()
cnt=0
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

def bfs():
    global cnt,sonic,water
    while sonic:
        for _ in range(len(water)):
            wx,wy=water.popleft()
            for i in range(4):
                nx=dx[i]+wx
                ny=dy[i]+wy
                if 0<=nx<R and 0<=ny<C and board[nx][ny]=='.' and not visit[nx][ny]:
                    visit[nx][ny]=True
                    water.append((nx,ny))
        cnt+=1
        for _ in range(len(sonic)):
            sx,sy=sonic.popleft()
            for i in range(4):
                nx=dx[i]+sx
                ny=dy[i]+sy
                if 0<=nx<R and 0<=ny<C and not visit[nx][ny]:
                    if board[nx][ny]=='.':
                        visit[nx][ny]=True
                        sonic.append((nx,ny))
                    elif board[nx][ny]=='D':
                        return print(cnt)

    return print("KAKTUS")

bfs()