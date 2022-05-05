import sys
from collections import deque
input=sys.stdin.readline
m,n=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
miro=[list(map(int,input().strip())) for _ in range(n)]
dist=[[-1]*m for _ in range(n)]
def bfs(i,j):
    q=deque()
    q.append((i,j))
    dist[i][j]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] 
            if 0<=nx<n and 0<=ny<m and dist[nx][ny]==-1:
                if miro[nx][ny]==1:
                    q.append((nx,ny))
                    dist[nx][ny]=dist[x][y]+1
                else:
                    q.appendleft((nx,ny))
                    dist[nx][ny]=dist[x][y]

bfs(0,0)
print(dist)