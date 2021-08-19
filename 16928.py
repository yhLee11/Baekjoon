from collections import deque
import sys
input=sys.stdin.readline
visited=[0 for _ in range(101)]
board=[0 for _ in range(101)]

n,m=map(int,input().split())

for _ in range(n):
    x,y=map(int,input().split())
    board[x]=y
for _ in range(m):
    u,v=map(int,input().split())
    board[u]=v
res=0
dq=deque()
dq.append((1,0))#시작지점, 주사위횟수
visited[1]=1
while dq:
    node=dq.popleft()
    if node[0]==100:
        res=min(res,node[1])
        continue

    for i in range(1,7):
        new=node[0]+i

        if new>100:
            continue
        if visited[new]==1:
            continue

        visited[new]==1

        if board[new]!=0:
            new=board[new]
        dq.append((new,node[1]+1))
        
print(res)
