import sys
from collections import deque
from copy import deepcopy as dc
input=sys.stdin.readline
n,m=map(int,input().split())
map=[list(map(int,input().strip())) for _ in range(n)]
wall_lst=[]
for i in range(n):
    for j in range(m):
        if map[i][j]==1:
            wall_lst.append((i,j))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
min_ans=sys.maxsize
def bfs(i,j,d):
    q=deque()
    q.append((i,j,d))
    distance=0
    isBreak=False
    while q:
        x,y,dis=q.popleft()
        visit[x][y]=True
        if (x,y)==(n-1,m-1):
            distance=dis
            break
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                if map[nx][ny]==1:
                    if not isBreak:
                        isBreak=True
                        q.append((nx,ny,dis+1))
                        visit[nx][ny]=True
                else:
                    q.append((nx,ny,dis+1))
                    visit[nx][ny]=True
    global min_ans
    min_ans=min(distance,min_ans)
    # print(min_ans)
                
visit=[[False]*m for _ in range(n)]
# bfs(0,0,1)
for wall in wall_lst:
    visit=[[False]*m for _ in range(n)]
    n_map=dc(map)
    n_map[wall[0]][wall[1]]=0
    bfs(0,0,1)
if min_ans==0:
    print(-1)
else:
    print(min_ans)

