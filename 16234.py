import sys
from collections import deque
input=sys.stdin.readline
N,L,R=map(int,input().split())
ctr=[list(map(int,input().split())) for _ in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(i,j):
    q=deque()
    q.append((i,j))
    mv=[(i,j)]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                if L<=abs(ctr[x][y]-ctr[nx][ny])<=R:
                    visit[nx][ny]=True
                    q.append((nx,ny))
                    mv.append((nx,ny))
    return mv
ans=0
while True:
    visit=[[False]*N for _ in range(N)]
    isTrue=False
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j]=True
                moved=bfs(i,j)
                if len(moved)>1:
                    isTrue=True
                    s=0
                    for x,y in moved:
                        s+=ctr[x][y]
                    s=s//len(moved)
                    for x,y in moved:
                        ctr[x][y]=s
    if not isTrue:
        break 
    ans+=1

print(ans)
    