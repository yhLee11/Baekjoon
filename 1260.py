from collections import deque
import sys
input=sys.stdin.readline

N,M,V=map(int,input().split())
node=[[] for _ in range(N+1)]
dfs_visit=[0 for _ in range(N+1)]
bfs_visit=[0 for _ in range(N+1)]
dfs_res,bfs_res=[],[]
dfs_res.append(V)
bfs_res.append(V)

for _ in range(M):
    a,b=map(int,input().split())
    node[a].append(b)
    node[b].append(a)

def dfs(start):
    for i in sorted(node[start]):
        if dfs_visit[i]==0:
            dfs_visit[i]=True
            dfs_res.append(i)
            # print(i,node[start])
            dfs(i)

def bfs(start):
    dq=deque(sorted(node[start]))
    while dq:
        # print(dq)
        n=dq.popleft()
        if not bfs_visit[n]:
            bfs_res.append(n)
            bfs_visit[n]=True
            dq.extend(sorted(node[n]))
            
# print(node)
dfs_visit[V]=True
dfs(V)
print(*dfs_res)

bfs_visit[V]=True
bfs(V)
print(*bfs_res)