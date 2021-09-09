"""https://pacific-ocean.tistory.com/364"""
import sys
input=sys.stdin.readline
h,w=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(h)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
mfinger=[[[0,1],[0,2],[-1,1]],[[0,1],[0,2],[1,1]],[[1,0],[2,0],[1,1]],[[1,0],[1,-1],[2,0]]]

visit=[[0]*w for _ in range(h)]
res=0
def dfs(x,y,cnt,num):
    global res
    if cnt==4:
        res=max(num,res)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<h and 0<=ny<w and visit[nx][ny]==0:
            visit[nx][ny]=1
            dfs(nx,ny,cnt+1,num+s[nx][ny])
            visit[nx][ny]=0
def middlefinger(x,y):
    global res
    for i in mfinger:
        try:
            num=s[x][y]+s[x+i[0][0]][y+i[0][1]]+s[x+i[1][0]][y+i[1][1]]+s[x+i[2][0]][y+i[2][1]]
        except:
            num=0
        res=max(res,num)

for i in range(h):
    for j in range(w):
        visit[i][j]=1
        dfs(i,j,1,s[i][j])
        visit[i][j]=0
        middlefinger(i,j)
print(res)
