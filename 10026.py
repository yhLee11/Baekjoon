import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
n=int(input())
grid=[list(input().strip()) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visit=[]
cnt1=0
cnt2=0
res=[]
def dfs(x,y):
    visit.append((x,y))
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and (nx,ny) not in visit:
            if grid[nx][ny]==grid[x][y]:
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if (i,j) not in visit:
            dfs(i,j)
            cnt1+=1

for i in range(n):
    for j in range(n):
        if grid[i][j]=='R':
            grid[i][j]='G'

visit=[]
for i in range(n):
    for j in range(n):
        if (i,j) not in visit:
            dfs(i,j)
            cnt2+=1
print(cnt1,cnt2)
