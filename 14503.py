import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
r,c,d=map(int,input().split())#0:북,1:동,2:남,3:서
arr=[list(map(int,input().split())) for _ in range(n)]
direct=[0,3,2,1]
dxy=deque([(0,-1),(1,0),(0,1),(-1,0)])#d=0일 때 순서
dic1={3:(0,-1),2:(1,0),1:(0,1),0:(-1,0)}
dic2={(0,-1):3,(1,0):2,(0,1):1,(-1,0):0}
visit=[[0]*m for _ in range(n)]
def sol(i,j,dr):
    global ans
    q=deque()
    q.append((i,j,dr))
    visit[i][j]=1
    while q:
        x,y,cdr=q.popleft()
        idx=3-cdr
        cnt=0
        for i in range(4):
            idx=(idx+1)%4
            # print(idx,dxy[idx])
            nx=dxy[idx][0]+x
            ny=dxy[idx][1]+y
            # print(nx,ny)
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0 and not visit[nx][ny]:
                visit[nx][ny]=1
                ndr=dic2[(dxy[idx][0],dxy[idx][1])]
                q.append((nx,ny,ndr))
                break
            else:cnt+=1
        if cnt==4:
            back=(cdr+2)%4
            a,b=dic1[back]
            if arr[x+a][y+b]!=1:
                q.append((x+a,y+b,cdr))
            else:
                return 
sol(r,c,d)
ans=0
for i in visit:
    ans+=sum(i)

print(ans)