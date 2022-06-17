import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
trust=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    trust[b].append(a)

def bfs(start):
    q=deque()
    q.append(start)
    visit=[False]*(n+1)
    cnt=1
    while q:
        node=q.popleft()
        for v in trust[node]:
            if not visit[v]:
                q.append(v)
                visit[v]=True
                cnt+=1
    return cnt
res=[]
maxcnt=-sys.maxsize
for i in range(1,n+1):
    tmp=bfs(i)
    maxcnt=max(maxcnt,tmp)
    res.append((i,tmp))
for i,cnt in res:
    if cnt==maxcnt:
        print(i,end=' ')