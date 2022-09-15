import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
trust=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    trust[b].append(a)

mx=0
res=[]

def bfs(start):
    q=deque()
    q.append(start)
    v=[False]*(n+1)
    v[start]=True
    cnt=1
    while q:
        cur=q.popleft()

        for nxt in trust[cur]:
            if not v[nxt]:
                v[nxt]=True
                q.append(nxt)
                cnt+=1
    return cnt

for st in range(1,n+1):
    cnt=bfs(st)
    mx=max(mx,cnt)
    res.append((st,cnt))

for s,c in res:
    if c==mx:
        print(s,end=' ')