import sys
from collections import deque
M,N,H=map(int,input().split())
box=[]
for i in range(H):
    oneN=[]
    for j in range(N):
        line=list(map(int, input().split()))
        oneN.append(line)
    box.append(oneN)
dx=[1,-1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
q=deque()
def bfs():
    while q:
        x,y,z=q.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and box[nz][nx][ny]==0:
                box[nz][nx][ny]=box[z][x][y]+1
                q.append([nx,ny,nz])
for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y]==1:
                q.append([x,y,z])
bfs()
res=-2
zero=False
for h in box:
    for m in h:
        for n in m:
            if n==0:
                zero=True
            res=max(res,n)
if zero==True:
    print(-1)
else:
    print(res-1)
