"""
https://deep-learning-study.tistory.com/581
https://pacific-ocean.tistory.com/349
"""
#dfs
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
k=int(input())

def dfs(v,group):
    visit[v]=group
    # print('visit[v]',visit[v])
    # print('group',group)
    for i in g[v]:
        if visit[i]==0:
            if not dfs(i,-group):
                print('-group',-group)
                return False
        elif visit[i]==visit[v]:#방문한 곳인데 그룹이 동일하면 False
            return False
    return True

for _ in range(k):
    v,e=map(int,input().split())
    g=[[] for i in range(v+1)]
    visit=[0]*(v+1)
    for _ in range(e):
        a,b=map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    isBipatite=True
    for i in range(1,v+1):
        if visit[i]==0:
            isBipatite=dfs(i,1)
            if not isBipatite:break
    print('YES' if isBipatite else 'NO')

#bfs1
from collections import deque
import sys
input=sys.stdin.readline
k=int(input())
for _ in range(k):
    v,e=map(int,input().split())
    g=[[] for _ in range(v+1)]
    for _ in range(e):
        a,b=map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    q=deque()
    visit=[0]*(v+1)
    isBipatite=True
    group=1
    for i in range(1,v+1):
        if visit[i]==0:
            q.append(i)
            visit[i]=group
            while q:
                vt=q.popleft()
                for j in g[vt]:
                    if visit[j]==0:
                        q.append(j)
                        visit[j]=-1*visit[vt]#현재노드와 다른그룹
                    elif visit[vt]==visit[j]:
                        isBipatite=False
    print('YES' if isBipatite else 'NO')

#bfs2
from collections import deque
import sys
input=sys.stdin.readline
k=int(input())
def bfs(start):
    visit[start]=1
    q=deque()
    q.append(start)
    while q:
        vt=q.popleft()
        for i in g[vt]:
            if visit[i]==0:
                visit[i]=-visit[vt]
                q.append(i)
            else:
                if visit[i]==visit[vt]:
                    return False
    return True

for _ in range(k):
    v,e=map(int,input().split())
    g=[[] for _ in range(v+1)]
    visit=[0]*(v+1)
    isBipatite=True
    for _ in range(e):
        a,b=map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    for k in range(1,v+1):
        if visit[k]==0:
            if not bfs(k):
                isBipatite=False
                break
    print('YES' if isBipatite else 'NO')
