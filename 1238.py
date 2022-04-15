import sys
import heapq as hq
from collections import defaultdict
input=sys.stdin.readline
n,m,x=map(int,input().split())
graph=defaultdict(dict)
visit=[False]*(n+1)
for i in range(n):
    graph[i+1]={}
for _ in range(m):
    s,e,t=map(int,input().split())
    graph[s][e]=t

def dijkstra(start):
    dist={node:float('inf') for node in graph}
    dist[start]=0
    visit[start]=True
    q=[]
    hq.heappush(q,(dist[start],start))
    
    while q:
        cur_dist,cur_node=hq.heappop(q)
        if dist[cur_node]<cur_dist:
            continue
        for new_node,new_dist in graph[cur_node].items():
            dt=cur_dist+new_dist
            if dt<dist[new_node]:
                dist[new_node]=dt
                hq.heappush(q,(dt,new_node))
    return dist

ans=[]
back=dijkstra(x)
max_num=-sys.maxsize
for i in range(n):
    res=dijkstra(i+1)
    max_num=max(max_num,res[x]+back[i+1])
print(max_num)