from re import X
import sys
from collections import deque
input=sys.stdin.readline
beer=20
t=int(input())
n=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(i,j,fesX,fesY):
    cnt=1
    q=deque()
    q.append((i,j))
    visit=[[0]*fesX for _ in range(fesY)]
    visit[i][j]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x 
            ny=dy[i]+y
            if 0<=nx<fesX and 0<=ny<fesY and not visit[nx][ny]:
                visit[nx][ny]=1
                

for i in range(t):
    # map=[[0]* for _ in range()]
    for j in range(n+2):
        homeX,homeY=map(int,input())
        for k in range(n):
            convX,convY=map(int,input())

        fesX,fesY=map(int,input().split())
    