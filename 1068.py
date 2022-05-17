import sys
input=sys.stdin.readline
n=int(input())
prt=list(map(int,input().split()))
dnode=int(input())

ans=0
def dfs(prt,dnode):
    prt[dnode]=-2
    # print(prt)
    for i in range(len(prt)):
        if dnode==prt[i]:
            dfs(prt,i)
dfs(prt,dnode)
ans=0
for i in prt:
    if i!=-1 and i!=-2:
        ans+=1
print(ans)
