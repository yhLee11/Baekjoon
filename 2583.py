import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]
cnt=0
def dfs(x,y):
    global cnt
    paper[x][y]=1
    cnt+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and paper[nx][ny]==0:
            dfs(nx,ny)

m,n,k=map(int,input().split())
paper=[[0]*n for _ in range(m)]
for i in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for r in range(m-y2,m-y1):
        for c in range(x1,x2):
            paper[r][c]=1
res=[]
for k in range(m):
    for p in range(n):
        if paper[k][p]==0:
            cnt=0
            dfs(k,p)
            res.append(cnt)

res.sort()
print(len(res))
print(*res)
