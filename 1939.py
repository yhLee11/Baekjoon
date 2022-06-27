import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
weight=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    weight[a].append((b,c))
    weight[b].append((a,c))
s,e=map(int,input().split())

def bfs(mid):
    global s,e
    q=deque()
    q.append(s)
    visit=[False]*(n+1)
    visit[s]=True
    while q:
        node=q.popleft()
        for x,w in weight[node]:
            if not visit[x] and w>=mid:
                visit[x]=True
                q.append(x)
    if visit[e]:
        return True
    else:
        return False
_min=1
_max=1000000000
res=_min
while _min<=_max:
    mid=(_min+_max)//2
    if bfs(mid):
        res=mid
        _min=mid+1
    else:
        _max=mid-1
print(res)

