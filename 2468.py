import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)#재귀의 최대 깊이
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y,h):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and mat[nx][ny]>h:
            visited[nx][ny]=True
            dfs(nx,ny,h)

n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
res=1
# print(max(map(max,mat)))
for line in range(max(map(max,mat))):
    visited=[[False]*n for _ in range(n)]
    safe_zone=0
    for i in range(n):
        for j in range(n):
            if mat[i][j]>line and visited[i][j]==False:
                safe_zone+=1
                visited[i][j]=True
                dfs(i,j,line)
    res=max(res,safe_zone)
print(res)
