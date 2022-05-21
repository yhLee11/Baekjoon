import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
s=[list(map(int,input().strip())) for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]
visit=[[[0]*2 for _ in range(m)] for _ in range(n)]
#visit[x][y][0]: 벽을 뚫지 않고 왔을 때 걸린 거리(시간)을 기록
#Visit[x][y][1]: 벽을 한 번이라도 뚫고 온 경우 걸린 거리(시간)을 기록
# 벽을 뚫지 않는 경우 [0]에 거리를 기록하다가 벽을 뚫고 [1]에 거리를 기록
def bfs(i,j,z):
    q=deque()
    q.append((i,j,z))
    visit[0][0][0]=1
    while q:
        x,y,c=q.popleft()
        if (x,y)==(n-1,m-1):
            return print(visit[x][y][c])
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m:
                if s[nx][ny]==1 and c==0:
                    visit[nx][ny][1]=visit[x][y][0]+1
                    q.append((nx,ny,1))
                elif s[nx][ny]==0 and visit[nx][ny][c]==0:
                    visit[nx][ny][c]=visit[x][y][c]+1
                    q.append((nx,ny,c))
    return print(-1)
bfs(0,0,0)