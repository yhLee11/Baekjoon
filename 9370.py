import sys
import heapq as hq
input=sys.stdin.readline

tc=int(input())
for _ in range(tc):
    n,m,t=map(int,input().split())#교차로,도로,목적지
    s,g,h=map(int,input().split())#출발지,지나간길(g-h)
    road=[[] for _ in range(n+1)]
    for i in range(m):
        a,b,d=map(int,input().split())
        if (a==g and b==h) or (a==h and b==g):
            road[a].append((b,d-0.1))
            road[b].append((a,d-0.1))
        else:
            road[a].append((b,d))
            road[b].append((a,d))
    candi=[int(input()) for _ in range(t)]#목적지 후보
    
    def dijkstra(start):
        dist=[float("inf") for _ in range(n+1)]
        dist[s]=0
        q=[]
        hq.heappush(q,(0,s))
        while q:
            cdist,cnode=hq.heappop(q)
            if dist[cnode]<cdist:continue
            for nn,nd in road[cnode]:
                cost=nd+dist[cnode]
                if cost<dist[nn]:
                    dist[nn]=cost
                    hq.heappush(q,(cost,nn))
        return dist
    
    sdks=dijkstra(s)
    ans=[]
    for c in candi:
        if sdks[c]!=float('inf') and type(sdks[c])==float:
            ans.append(c)
    ans.sort()
    print(*ans)