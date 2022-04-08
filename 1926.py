import sys
from collections import deque
input=sys.stdin.readline
h,w = map(int,input().split())
map=[list(map(int,input().split())) for _ in range(h)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
maxcnt=-sys.maxsize
v=[[False]*w for _ in range(h)]

def bfs(a,b):
    q=deque()
    q.append((a,b))
    v[a][b]=True
    size=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<h and 0<=ny<w and map[nx][ny] and not v[nx][ny]:
                v[nx][ny]=True
                q.append((nx,ny))
                size+=1
    global maxcnt
    maxcnt=max(size,maxcnt)

painting=0
for i in range(h):
    for j in range(w):
        if map[i][j] and not v[i][j]:
            bfs(i,j)
            painting+=1
if not painting:
    print(0)
    print(0)
    return 
print(painting)
print(maxcnt)
