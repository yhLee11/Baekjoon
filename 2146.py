import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
cnt=2
def bfs1(i,j):
    global cnt
    q=deque()
    q.append((i,j))
    visit=[[False]*n for _ in range(n)]
    visit[i][j]=True
    board[i][j]=cnt
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and board[nx][ny]==1:
                q.append((nx,ny))
                visit[nx][ny]=True
                board[nx][ny]=cnt
    cnt+=1
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            bfs1(i,j)

min_dist=sys.maxsize
def bfs2(start):
    global min_dist
    q=deque()
    distance=[[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]==start:
                distance[i][j]=0
                q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]==0 and distance[nx][ny]==-1:
                    q.append((nx,ny))
                    distance[nx][ny]=distance[x][y]+1
                   
                if board[nx][ny]!=start and board[nx][ny]>0:
                    min_dist=min(distance[x][y],min_dist)
                    return


for i in range(2,cnt):
    bfs2(i)
print(min_dist)
