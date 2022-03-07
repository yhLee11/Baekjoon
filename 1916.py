import heapq
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
INF=sys.maxsize
city=[[] for _ in range(n+1)]
q=[INF for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    city[a].append([b,c])

start,end=map(int,input().split())

def dijkstra(start):
    q[start]=0
    heap=[]
    heapq.heappush(heap,[0,start])
    while heap:
        w,n=heapq.heappop(heap)
        if q[n]<w:
            continue
        for nn,we in city[n]:
            nw=w+we
            if q[nn]>nw:
                q[nn]=nw
                heapq.heappush(heap,[nw,nn])
dijkstra(start)
print(q[end])