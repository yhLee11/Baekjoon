import sys
import heapq as hq
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dijkstra(start):
    dist=[float("inf") for _ in range(n+1)]
    dist[start]=0
    q=[]
    hq.heappush(q,(0,start))
    while q:
        cdist,cnode=hq.heappop(q)
        if dist[cnode]<cdist:continue
        for nn,nd in graph[cnode]:
            cost=nd+cdist
            if cost<dist[nn]:
                dist[nn]=cost
                hq.heappush(q,(cost,nn))
    return dist
d=dijkstra(1)
md=max(d[1:])
md_idx=d.index(md)
ans=max(dijkstra(md_idx)[1:])
#가장 긴 구간을 포함하는 도착지로부터 다시 다익스트라 알고리즘 사용
print(ans)
