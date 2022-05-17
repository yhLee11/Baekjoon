import sys
import heapq as hq
input=sys.stdin.readline
v=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(v):
    lst=list(map(int,input().split()))
    n=lst[0]
    lst=lst[1:-1]
    for i in range(0,len(lst),2):
        graph[n].append([lst[i],lst[i+1]])

def dijkstra(start):
    dist=[float('inf') for _ in range(v+1)]
    q=[]
    dist[start]=0
    hq.heappush(q,(0,start))
    while q:
        cdist,cnode=hq.heappop(q)
        if dist[cnode]<cdist:continue
        for nn,nd in graph[cnode]:
            cost=nd+dist[cnode]
            if dist[nn]>cost:
                dist[nn]=cost
                hq.heappush(q,(cost,nn))
    return dist

d=dijkstra(1)[1:]
d_max=max(d)
d_idx=d.index(d_max)
ans=max(dijkstra(d_idx+1)[1:])
print(ans)
