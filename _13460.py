import sys
from collections import deque
input=sys.stdin.readline
h,w=map(int,input().split())
B=[list(input().strip()) for _ in range(h)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
rx,ry,bx,by=0,0,0,0
for i in range(h):
    for j in range(w):
        if B[i][j]=='R':
            rx=i
            ry=j
        elif B[i][j]=='B':
            bx=i
            by=j
        
def move(x,y,dx,dy):
    cnt=0
    while B[x+dx][y+dy]!='#' and B[x][y]!='O':
        x+=dx
        y+=dy
        cnt+=1
    return x,y,cnt

def bfs():
    q=deque()
    q.append((rx,ry,bx,by,1))
    v=[[[[False]*w for _ in range(h)] for _ in range(w)] for _ in range(h)]
    v[rx][ry][bx][by]=True
    while q:
        a,b,c,d,cnt=q.popleft()
        if cnt>10:break
        for i in range(4):
            nrx,nry,rcnt=move(a,b,dx[i],dy[i])
            nbx,nby,bcnt=move(c,d,dx[i],dy[i])

            if B[nbx][nby]!='O':
                if B[nrx][nry]=='O':
                    print(cnt)
                    return
                if (nrx,nry)==(nbx,nby):
                    if rcnt<bcnt:
                        nbx-=dx[i]
                        nby-=dy[i]
                    elif rcnt>bcnt:
                        nrx-=dx[i]
                        nry-=dy[i]
            
                if not v[nrx][nry][nbx][nby]:
                    v[nrx][nry][nbx][nby]=True
                    q.append((nrx,nry,nbx,nby,cnt+1))
    print(-1)
bfs()
            