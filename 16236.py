from dis import dis
from math import dist
import sys
from collections import deque
input=sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n=int(input())
sea=[list(map(int,input().split())) for _ in range(n)]
visit=[[False]*n for _ in range(n)]
#9: baby shark
#0: empty
baby_shark=2
up=0

def bfs(i,j,dist):
    global up,baby_shark
    q=deque()
    q.append((i,j,dist))
    stk=[]
    visit=[[False]*n for _ in range(n)]
    visit[i][j]=True
    while q:
        x,y,d=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                visit[nx][ny]=True
                if sea[nx][ny]<=baby_shark:
                    q.append((nx,ny,d+1))
                if sea[nx][ny]<baby_shark and sea[nx][ny]!=0:
                    stk.append((d+1,nx,ny))#거리,좌표,크기
    if stk:
        stk.sort(key=lambda x:(x[0],x[1],x[2]))
        up+=1
        if baby_shark==up:
            baby_shark+=1
            up=0
        return stk[0]#restart point
    else:
        return (-1,-1,-1)

for i in range(n):
    for j in range(n):
        if sea[i][j]==9:#아기상어 발견!
            start=(i,j)
            sea[i][j]=2
            break 
moveTime=0            
while True:
    i,j=start[0],start[1]
    distance,a,b=bfs(i,j,0)
    if distance==-1:
        break

    moveTime+=distance
    start=(a,b)
    sea[a][b]=0
    
print(moveTime)