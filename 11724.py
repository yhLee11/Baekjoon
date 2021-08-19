from collections import deque
import sys
input=sys.stdin.readline
def bfs():
    q=deque()
    res=0
    for i in range(1,n+1):
        if visited[i]==0:
            visited[i]=1
            q.append(i)
            res+=1

            while q:
                cur=q.popleft()
                for j in graph[cur]:
                    if visited[j]==0:
                        visited[j]=1
                        q.append(j)
    print(res)


n,m=map(int,input().split())
visited=[False]*(n+1)
graph=[[0]*n for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
bfs()
