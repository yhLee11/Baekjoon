import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
k=int(input())

def dfs(v,g):
    visit[v]=g
    for i in g[v]:
        if visit[i]==0:
            if not dfs(i,-g):
                return False
        elif visit[i]==visit[v]:
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