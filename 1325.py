import sys
from collections import deque
input=sys.stdin.readline
#sys.setrecursionlimit(100000)
n,m=map(int,input().split())
trust=[[] for _ in range(n+1)]

def bfs(node):
    q=deque()
    q.append(node)
    visit[node]=1
    while q:
        node=q.popleft()
        for n in trust[node]:
            if visit[n]==0:
                visit[n]=1
                q.append(n)


for i in range(m):
    a,b=map(int,input().split())
    trust[a]+=[b]
res=[]
for i in range(1,n+1):
    visit=[0 for _ in range(n+1)]
    bfs(i)
    # print('visit',visit)
    res.append(visit.count(1))
# print(res)
m=max(res)
for i in range(n):
    if res[i]==m:
        print(i+1,end=" ")
print()
