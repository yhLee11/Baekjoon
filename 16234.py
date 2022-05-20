from itertools import count
import sys
from collections import deque
input=sys.stdin.readline
N,L,R=map(int,input().split())
country=[list(map(int,input().split())) for _ in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
visit=[[False]*N for _ in range(N)]
flag=False

def bfs(i,j):
    move=[(i,j)]
    q=deque()
    q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                if L<=abs(country[x][y]-country[nx][ny])<=R:
                    visit[nx][ny]=True
                    q.append((nx,ny))
                    move.append((nx,ny))
    return move
cnt=0
while True:
    visit=[[False]*N for _ in range(N)]
    isTrue=False
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j]=True
                tmp=bfs(i,j)
                if len(tmp)>1:
                    isTrue=True
                    num=sum([country[x][y] for x,y in tmp])//len(tmp)
                    for x,y in tmp:
                        country[x][y]=num
    if not isTrue:
        break
    cnt+=1                
print(cnt)