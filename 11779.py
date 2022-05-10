import sys
import heapq as hq
input=sys.stdin.readline
n=int(input())
m=int(input())
INF=float("inf")
graph=[[] for _ in range(n+1)]
dist=[INF for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
start,end=map(int,input().split())
route=[i for i in range(n+1)]

def dijkstra(start):
    global route
    dist[start]=0
    q=[]
    hq.heappush(q,(dist[start],start))
    while q:
        cdist,cnode=hq.heappop(q)
        if dist[cnode]<cdist:continue
        for nn,nd in graph[cnode]:
            cost=dist[cnode]+nd
            if cost<dist[nn]:
                dist[nn]=cost
                route[nn]=cnode
                hq.heappush(q,(cost,nn))

dijkstra(start)

print(dist[end])
st=[]
cnt=1
i=end
st.append(i)
while i!=start:
    i=route[i]
    cnt+=1
    st.append(i)
print(cnt)
while st:
    print(st.pop(),end=' ')