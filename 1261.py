import sys
import heapq as hq
input=sys.stdin.readline
m,n=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
miro=[list(map(int,input().strip())) for _ in range(n)]

def dijkstra(start):
    q=[]
    dist=[]
    hq.heappush(q,(dist[start],start))
    cur_dist,cur_node=hq.heappop(q)
    