import sys
from collections import deque
from this import d
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]

def bfs(i,j):
    dq=deque()
    dq.append((i,j))
    while dq:
        x,y=dq.popleft()
        adjSea=0
        if maps[x][y]:
            for i in range(4):
                nx=dx[i]+x
                ny=dy[i]+y
                if 0<=nx<n and 0<=ny<m and not maps[nx][ny]:#0
                    adjSea+=1
        minus[x][y]=adjSea
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] and not visit[nx][ny]:
                visit[nx][ny]=1
                dq.append((nx,ny))

cnt=0
iceberg=0
while True:
    iceberg=0
    visit=[[0]*m for _ in range(n)]
    minus=[[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] and not visit[i][j]:
                visit[i][j]=1
                bfs(i,j)
                iceberg+=1

    if iceberg==0:
        print(cnt)
        break
    elif iceberg>1:
        print(cnt)
        break

    for i in range(n):
        for j in range(m):
            maps[i][j]-=minus[i][j]
            if maps[i][j]<0:
                maps[i][j]=0
    temp=0
    for i in range(n):
        temp+=sum(maps[i])
    if temp==0:
        print(0)
        break

    cnt+=1