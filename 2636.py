import sys
from collections import deque
input=sys.stdin.readline
h,w=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(h)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(i,j):
    q=deque()
    q.append((i,j))
    visit=[[False]*w for _ in range(h)]
    visit[i][j]=True
    cnt=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<h and 0<=ny<w and not visit[nx][ny]:
                if board[nx][ny]==0:
                    visit[nx][ny]=True
                    q.append((nx,ny))
                elif board[nx][ny]==1:
                    board[nx][ny]=0
                    visit[nx][ny]=1
                    cnt+=1
    return cnt
ans=[]
while True:
    tmp=bfs(0,0)
    if tmp==0:break
    ans.append(tmp)
print(len(ans))
print(ans[-1])