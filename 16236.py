import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
sea=[]
sum=0
for i in range(n):
    sea.append(list(map(int, input().split())))
    for j in sea[i]:
        sum+=j
if sum==9:
    print(0)
    exit()

chk=[[0 for i in range(n)] for j in range(n)]
#위, 왼, 아래, 오른
dx=[-1,0,1,0]
dy=[0,-1,0,1]
shk=2#가장 처음의 아기상어 크기는 2
time=0

q=deque([0,0])
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and chk[nx][ny]==0:
            if 
