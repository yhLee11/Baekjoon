import sys
input=sys.stdin.readline
N=int(input())
lst=[input().strip() for _ in range(N)]
v=[[0]*N for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:continue
            if lst[i][j]=='Y' or (lst[i][k]=='Y' and lst[k][j]=='Y'):
                v[i][j]=1
res=0
for i in range(N):
    res=max(res,sum(v[i]))
print(res)