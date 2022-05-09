import sys
import heapq as hq
input=sys.stdin.readline
n,k=map(int,input().split())
INF=float("inf")
dist=[INF for _ in range(100001)]
# graph=[[] for _ in range(100001)] 
weight=[-1,1,2]
# for i in range(100001):
#     graph[i].append((i+1,1))
#     graph[i].append((i-1,1))
#     graph[i].append((i*2,0))

def dijkstra(start):
    dist[start]=0
    q=[]
    hq.heappush(q,(dist[start],start))
    while q:
        cdist,cnode=hq.heappop(q)
        if cnode==k:
            return 
        if cdist>dist[cnode]:
            continue
        for i in range(3):
            if i==2:
                nn=cnode*weight[i]
                nd=0
            else:
                nn=cnode+weight[i]
                nd=1
            if nn<0 or nn>100000:
                continue
            
            cost=nd+cdist
            if dist[nn]>cost:
                dist[nn]=cost
                hq.heappush(q,(cost,nn))

            
        # for nn,nd in graph[cnode]:
        #     if nn<0 or nn>100000:
        #         continue
        #     print(nn,nd)
        #     cost=nd+dist[cnode]
        #     if cost<dist[nn]:
        #         dist[nn]=cost
        #         hq.heappush(q,(cost,nn))
   
dijkstra(n)
print(dist[k])
