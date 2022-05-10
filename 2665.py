import sys
import heapq as hq
input=sys.stdin.readline
n=int(input())
room=[list(map(int,list(input().strip()))) for _ in range(n)]
INF=float("inf")
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dijkstra(i,j):
    q=[]    
    hq.heappush(q,(0,i,j))
    visit=[[False]*n for _ in range(n)]
    while q:
        c,x,y=hq.heappop(q)
        if (x,y)==(n-1,n-1):
            return c
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                if room[nx][ny]==0:
                    hq.heappush(q,(c+1,nx,ny))
                else:
                    hq.heappush(q,(c,nx,ny))
                visit[nx][ny]=True
cnt=dijkstra(0,0)
print(cnt)