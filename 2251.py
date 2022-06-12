import sys
from collections import deque
input=sys.stdin.readline
a,b,c=map(int,input().split())
ans=[]
q=deque()
q.append((0,0))
visit=[[0]*(b+1) for _ in range(a+1)]
visit[0][0]=1
def pour(x,y):
    if not visit[x][y]: 
        visit[x][y]=True
        q.append((x,y))
def bfs():
    while q:
        x,y=q.popleft()
        z=c-x-y#c의 물양
        if x==0:
            ans.append(z)
        #x->y
        water=min(x,b-y)
        pour(x-water,y+water)
        #x->z
        water=min(x,c-z)
        pour(x-water,y)
        #y->x
        water=min(y,a-x)
        pour(x+water,y-water)
        #y->z
        water=min(y,c-z)
        pour(x,y-water)
        #z->x
        water=min(z,a-x)
        pour(x+water,y)
        #z->y
        water=min(z,b-y)
        pour(x,y+water)
bfs()
print(' '.join(map(str,sorted(ans))))