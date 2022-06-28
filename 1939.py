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

#bfs: s->e 까지의 최단 경로
def bfs(mid):
    global s,e
    q=deque()
    q.append(s)
    visit=[False]*(n+1)
    visit[s]=True
    while q:
        cur=q.popleft()
        for nxt,wet in weight[cur]:
            if not visit[nxt] and wet>=mid:
                visit[nxt]=True
                q.append(nxt)
    if visit[e]:
        return True
    else:
        return False

min=1
max=1000000000
ans=0
while min<=max:
    mid=(min+max)//2
    if bfs(mid):
        ans=mid
        min=mid+1
    else:
        max=mid-1
print(ans)
