import sys
import heapq as hq
input=sys.stdin.readline
tc=int(input())
for _ in range(tc):
    n,d,c=map(int,input().split())
    com=[[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s=map(int,input().split())
        com[b].append((a,s))
    
    cnt=[]
    q=[]
    dist=[float('inf') for _ in range(n+1)]
    hq.heappush(q,(0,c))
    while q:
        cdist,cnode=hq.heappop(q)
        cnt.append(cnode)
        if dist[cnode]<cdist:continue
        for nn,nd in com[cnode]:
            cost=nd+cdist
            if cost<dist[nn]:
                dist[nn]=cost
                hq.heappush(q,(cost,nn))
    print(len(set(cnt)),dist[-1])