li=[list(map(str,input().split())) for _ in range(5)]
res=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

stk=[(0,0)]
res=[]
def dfs(x,y,nstr):
    if len(nstr)==6:
        if nstr not in res:
            res.append(nstr)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,nstr+li[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i,j,li[i][j])
print(len(res))
