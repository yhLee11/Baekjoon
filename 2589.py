import sys
from collections import deque
input=sys.stdin.readline
r,c=map(int,input().split())
board=[list(input().strip()) for _ in range(r)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
max_cnt=-sys.maxsize
def bfs(i,j,cnt):
    global max_cnt
    q=deque()
    q.append((i,j,cnt))
    visit=[[False]*c for _ in range(r)]
    visit[i][j]=True
    while q:
        x,y,ct=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<r and 0<=ny<c and board[nx][ny]=='L' and not visit[nx][ny]:
                visit[nx][ny]=True
                max_cnt=max(max_cnt,ct+1)
                q.append((nx,ny,ct+1))

for i in range(r):
    for j in range(c):
        if board[i][j]=="L":
            bfs(i,j,0)
print(max_cnt)