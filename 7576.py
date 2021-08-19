from collections import deque
m,n=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
q=deque()

dx=[1,-1,0,0]
dy=[0,0,-1,1]
def bfs():
    while q:
        x,y=q.popleft()
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0:
                arr[nx][ny]=arr[x][y]+1
                q.append([nx,ny])
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            q.append([i,j])
bfs()
zero=False
res=-2
for i in arr:
    for j in i:
        if j==0:
            zero=True
        res=max(res,j)
if zero==True:
    print(-1)
elif res==-1:
    print(0)
else:
    print(res-1)
