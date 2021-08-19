from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())

board=[]
for _ in range(n):
    board.append(list(input().strip()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
dq=deque()
dq.append((0,0))
while dq:
    x,y=dq.popleft()
    # print(x,y)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]=="1":
            dq.append((nx,ny))
            board[nx][ny]=str(int(board[x][y])+1)
print(board[n-1][m-1])
