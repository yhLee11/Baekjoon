import sys
import heapq
input=sys.stdin.readline
V,E=map(int,input().split())
k=int(input().strip())
INF=int(1e9)
#graph={}
graph=[[] for _ in range(V+1)]
for i in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))

dist=[INF]*(V+1)
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        c_dist,c_node=heapq.heappop(q)
        #print('c_node',c_node)
        if dist[c_node]<c_dist:
            continue
        for i in graph[c_node]:
            cost=c_dist+i[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(k)
# print(dist)
# print(graph)
for i in range(1,V+1):
    if dist[i]==INF:
        print('INF')
    else:
        print(dist[i])
