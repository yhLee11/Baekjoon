import sys
from collections import deque
input=sys.stdin.readline
h,w=map(int,input().split())
s=[list(input().strip()) for _ in range(h)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
red,blue=(),()
for i in range(h):
    for j in range(w):
        if red!=() and blue!=():
            break
        if s[i][j]=='R':
            red=(i,j)
        elif s[i][j]=='B':
            blue=(i,j)
visit=[[[[False]*w] for _ in range(h)] for _ in range(w)]

def move(x,y,dx,dy):
    cnt=0
    while s[x+dx][y+dy]!='#' and s[x][y]!='O':
        x+=dx
        y+=dy
        cnt+=1
    return x,y,cnt

def bfs():
    q=deque()
    q.append((red[0],red[1],blue[0],blue[1],1))
    while q:
        rx,ry,bx,by,depth=q.popleft()
        if depth>10:
            break
        for i in range(4):
            rnx,rny,rcnt=move(rx,ry,dx[i],dy[i])
            bnx,bny,bcnt=move(bx,by,dx[i],dy[i])
            if s[bnx][bny]!='O':
                if s[rnx][rny]=='O':
                    print(depth)
                    return
                if rnx==bnx and rny==bny:
                    if rcnt>bcnt:
                        rnx-=dx[i]
                        rny-=dy[i]
                    else:
                        bnx-=dx[i]
                        bny-=dx[i]

                if not visit[rnx][rny][bnx][bny]:
                    visit[rnx][rny][bnx][bny]=True
                    q.append((rnx,rny,bnx,bny,depth+1))
    print(-1)
bfs()