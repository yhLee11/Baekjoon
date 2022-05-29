import sys
from collections import deque
input=sys.stdin.readline
h,w=map(int,input().split())
s=[list(input().strip()) for _ in range(h)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(i,j):
    q=deque([(i,j)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            
            if s[nx][ny]
