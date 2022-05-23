import sys
input=sys.stdin.readline
def bellman_ford(start):
    dist[start]=0
    for i in range(1,n+1):
        for s in range(1,n+1):
            for nnode,cost in graph[s]:
                if dist[nnode]>dist[s]+cost:
                    dist[nnode]=dist[s]+cost
                    if i==n:
                        return True
    return False

tc=int(input())
for _ in range(tc):
    n,m,w=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    dist=[10001 for _ in range(n+1)]

    for _ in range(m):
        s,e,t=map(int,input().split())
        graph[s].append((e,t))
        graph[e].append((s,t))
    for _ in range(w):
        s,e,t=map(int,input().split())
        graph[s].append((e,-t))
    if bellman_ford(1):
        print("YES") 
    else:
        print("NO")       