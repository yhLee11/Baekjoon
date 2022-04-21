from itertools import count
import sys
from collections import deque
from xml.dom import xmlbuilder
input=sys.stdin.readline
N,L,R=map(int,input().split())
country=[list(map(int,input().split())) for _ in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
visit=[[False]*N for _ in range(N)]
def bfs(i,j):
    cnt=1
    move=[(i,j)]
    all=country[i][j]
    q=deque()
    q.append((i,j,cnt))
    while q:
        x,y,c=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                if L<=abs(country[x][y]-country[nx][ny])<=R:
                    visit[nx][ny]=True
                    q.append((nx,ny,c+1))
                    all+=country[nx][ny]
                    move.append((nx,ny))
    num=int(all/c)
    for m1,m2 in move:
        country[m1][m2]=num

flag=False
while True:
    visit=[[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                bfs(i,j)
