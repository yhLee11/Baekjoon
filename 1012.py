from collections import deque
import sys
input=sys.stdin.readline
t=int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(a,b):
    q=deque()
    q.append((a,b))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w and board[nx][ny]==1:
                board[nx][ny]=0
                q.append((nx,ny))

for _ in range(t):
    cnt=0
    w,h,k=map(int,input().split())
    board=[[0]*w for _ in range(h)]
    for _ in range(k):
        x,y=map(int,input().split())
        board[y][x]=1

    for a in range(h):
        for b in range(w):
            if board[a][b]==1:
                bfs(a,b)
                board[a][b]=0
                cnt+=1
    print(cnt)
