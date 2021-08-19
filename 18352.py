import sys
import heapq
input=sys.stdin.readline
n,m,k,x=map(int,input().split())
INF=int(1e9)

graph=[[] for _ in range(n+1)]
for i in range(m):
    s,e=map(int,input().split())
    graph[s].append((e,1))

#print(graph)

dist=[INF]*(n+1)
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0

    while q:
        c_dist,c_node=heapq.heappop(q)
        if dist[c_node]<c_dist:
            continue
        for i in graph[c_node]:
            cost=c_dist+i[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(x)
cnt=0
for i in range(1,n+1):
    if dist[i]==k:
        print(i)
        cnt+=1
if cnt==0:
    print(-1)
