import sys
input=sys.stdin.readline
n,m=map(int,input().split())
city=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    city[a].append((b,c))
INF=float('inf')
def bf(start):
    dist=[INF for _ in range(n+1)]
    dist[start]=0
    for i in range(1,n+1):
        for cnode in range(1,n+1):
            for nnode,cost in city[cnode]:
                if dist[nnode]>cost+dist[cnode]:
                    dist[nnode]=cost+dist[cnode]
                    if i==n:
                        return False
    # for cnode in range(1,n+1):
    #     for v,c in city[cnode]:
    #         if dist[v]>dist[cnode]+c:
    #             return False
        
    return dist

ans=bf(1)
# print(ans)
isTrue=False
if ans==False:
    print(-1)
else:
    for i in range(2,n+1):
        print(ans[i] if ans[i]<INF else -1)