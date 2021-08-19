n=int(input())
con=int(input())
a=[[0]*(n+1) for i in range(n+1)]
seen=[0]*(n+1)
res=[]
for i in range(con):
    c,r = map(int, input().split())
    a[c][r]=1
    a[r][c]=1
def dfs(v):
    seen[v]=1
    for i in range(1,n+1):
        if a[v][i]==1 and seen[i]==0:
            res.append(i)
            dfs(i)
    return len(res)
print(dfs(1))
