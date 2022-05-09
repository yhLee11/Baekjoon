import sys
import heapq as hq
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]
INF=float("inf")
cnt=1
while True:
    size=int(input())
    if size==0:break
    cave=[list(map(int,input().split())) for _ in range(size)]
    dist=[[INF]*size for _ in range(size)]
    dist[0][0]=cave[0][0]
    q=[]
    hq.heappush(q,(cave[0][0],(0,0)))
    while q:
        r,(x,y)=hq.heappop(q)
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<size and 0<=ny<size:
                cost=r+cave[nx][ny]
                if cost<dist[nx][ny]:
                    dist[nx][ny]=cost
                    hq.heappush(q,(cost,(nx,ny)))
    print("Problem "+str(cnt)+": "+str(dist[-1][-1]))
    cnt+=1