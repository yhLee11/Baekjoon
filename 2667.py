from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
map=[]
for _ in range(n):
    map.append(list(input().strip()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
res=[]

def bfs(i,j):
    global res
    cnt=1
    q=deque()
    q.append((i,j))
    map[i][j]="0"
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and map[nx][ny]=="1":
                cnt+=1
                map[nx][ny]="0"
                q.append((nx,ny))
    res+=[cnt]

for i in range(n):
    for j in range(n):
        if map[i][j]=="1":
            bfs(i,j)
res.sort()
print(len(res))
for i in res:
    print(i)
