import sys
from collections import deque
input=sys.stdin.readline
N,M,K=map(int,input().split())
road=[[0]*M for _ in range(N)]
for _ in range(K):
    a,b=map(int,input().split())
    road[a-1][b-1]=1
dx=[0,0,1,-1]
dy=[1,-1,0,0]
ans=float('-inf')
def bfs(i,j):
    global ans
    q=deque()
    q.append((i,j))
    road[i][j]=2
    v=[[False]*M for _ in range(N)]
    v[i][j]=True
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<N and 0<=ny<M and not v[nx][ny] and road[nx][ny]==1:
                v[nx][ny]=True
                road[nx][ny]==2
                q.append((nx,ny))
                cnt+=1
    ans=max(ans,cnt)
for i in range(N):
    for j in range(M):
        if road[i][j]==1:
            bfs(i,j)
print(ans)