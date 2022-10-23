import sys
input=sys.stdin.readline
N=int(input())
path=list(input().split())
dx=[0,0,1,-1]#R L D U
dy=[1,-1,0,0]#우 좌 아 위
x,y=0,0
nx,ny=0,0
for i in path:
    if i=="R":
        nx=dx[0]+x
        ny=dy[0]+y
        if not (0<=nx<N and 0<=ny<N):
            nx-=dx[0]
            ny-=dy[0]
    elif i=="L":
        nx=dx[1]+x
        ny=dy[1]+y
        if not (0<=nx<N and 0<=ny<N):
            nx-=dx[1]
            ny-=dy[1]
    elif i=="D":
        nx=dx[2]+x
        ny=dy[2]+y
        if not (0<=nx<N and 0<=ny<N):
            nx-=dx[2]
            ny-=dy[2]
    else:
        nx=dx[3]+x
        ny=dy[3]+y
        if not (0<=nx<N and 0<=ny<N):
            nx-=dx[3]
            ny-=dy[3]
    x=nx
    y=ny
print(x+1,y+1)

# 해설
x,y=1,1
move=["R","L","D","U"]
for p in path:
    for m in range(4):
        if p==move[m]:
            nx=x+dx[m]
            ny=y+dy[m]
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    x,y=nx,ny
print(x,y)
