# 두칸가고 한칸 왼,오
# (2,2)->(1,0) -1,-2
# (2,2)->(0,1) -2,-1
# (2,2)->(0,3) -2,+1
# (2,2)->(1,4) -1,+2
# (2,2)->(3,0) +1,+2
# (+-1,+-2),(+-2,+-1)
import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
dx=[1,-1,2,-2,2,-2,1,-1]
dy=[2,-2,1,-1,-1,1,-2,2]
res=[]
def bfs(sx,sy,ex,ey,l,chess):
    q=deque()
    q.append((sx,sy))
    chess[sx][sy]=1
    while q:
        x,y=q.popleft()
        if x==ex and y==ey:
            res.append(chess[x][y]-1)
            break
        for i in range(8):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<l and 0<=ny<l and not chess[nx][ny]:
                chess[nx][ny]=chess[x][y]+1
                q.append((nx,ny))

for i in range(n):
    l=int(input())
    chess=[[0]*l for _ in range(l)]
    startX,startY = map(int,input().split())
    endX,endY = map(int,input().split())
    chess[startX][startY]=1

    bfs(startX,startY,endX,endY,l,chess)

for r in res:
    print(r)