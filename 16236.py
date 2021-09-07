#참고:https://pacific-ocean.tistory.com/377
import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
sea=[list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#9:baby shark
#0: empty

def bfs(i,j):
    q=deque()
    q.append([i,j])
    visit=[[0]*n for _ in range(n)]
    visit[i][j]=1
    eat=[]
    dist=[[0]*n for _ in range(n)]
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=dx[k]+x
            ny=dy[k]+y

            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
                # print(nx,ny)
                if sea[nx][ny]<=sea[x][y] or sea[nx][ny]==0:
                    q.append([nx,ny])
                    visit[nx][ny]=1
                    dist[nx][ny]=dist[x][y]+1
                # print(sea[x][y],sea[nx][ny])
                if sea[nx][ny]<sea[i][j] and sea[nx][ny]!=0:
                    print('eat')
                    eat.append([nx,ny,dist[nx][ny]])
    print(eat)
    if not eat:
        return -1,-1,-1

    eat.sort(key=lambda x:(x[2],x[0],x[1]))#가까운거리,가장위(y),가장왼쪽(x)
    return eat[0][0],eat[0][1],eat[0][2]

for i in range(n):
    for j in range(n):
        if sea[i][j]==9:
            start=[i,j]
            sea[i][j]=2
            break
exp=0
cnt=0
while True:
    i,j=start[0],start[1]
    ex,ey,dist=bfs(i,j)
    if ex==-1: break
    print(ex,ey,sea[ex][ey])
    print(i,j,sea[i][j])
    sea[ex][ey]=sea[i][j]#이건왜?
    sea[i][j]=0
    start=[ex,ey]
    exp+=1
    if exp==sea[ex][ey]:
        exp=0
        sea[ex][ey]+=1
    cnt+=dist

print(cnt)
