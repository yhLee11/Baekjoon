import sys
from collections import deque
input=sys.stdin.readline
#맨해튼 거리: abs(x2-x1)+abs(y2-y1)
t=int(input())

def bfs(i,j):
    dq=deque()
    dq.append((i,j))
    while dq:
        a,b=dq.popleft()
        if abs(a-festX)+abs(b-festY)<=1000:
            print("happy")
            return
        for i in range(n):
            if not visit[i]:
                nx,ny=conv[i]
                if abs(nx-a)+abs(ny-b)<=1000:
                    dq.append((nx,ny))
                    visit[i]=1
                
    print("sad")        
    return 
for _ in range(t):
    n=int(input())
    conv=[]#coordinates
    homeX,homeY=map(int,input().split())
    for _ in range(n):
        x,y=map(int,input().split())
        conv.append([x,y])
    festX,festY=map(int,input().split())
    visit=[0 for _ in range(n)]
    bfs(homeX,homeY)
