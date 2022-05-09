import sys
import heapq as hq
INF=float("inf")
n,e=map(int,input().split())
graph=[[]*n for _ in range(n+1)]
for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append([a,c])

v1,v2=map(int,input().split())

def dijkstra(start):#시작 노드 
    dist=[INF]*(n+1)
    dist[start]=0
    q=[]
    hq.heappush(q,(dist[start],start))
    while q:
        cdist,cnode=hq.heappop(q)
        if dist[cnode]<cdist:continue   
        for nxt in graph[cnode]:
            cost=dist[cnode]+nxt[1]

            if cost < dist[nxt[0]]:
                dist[nxt[0]]=cost
                hq.heappush(q,(cost,nxt[0]))
    return dist
dist=dijkstra(1)#1->N
v1_dist=dijkstra(v1)#v1->N
v2_dist=dijkstra(v2)#v2->N
print(dist,v1_dist,v2_dist)
ans=min(dist[v1]+v1_dist[v2]+v2_dist[n],dist[v2]+v2_dist[v1]+v1_dist[n])
