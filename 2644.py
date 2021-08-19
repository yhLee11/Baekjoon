import sys
from collections import deque
sys.setrecursionlimit(100000)
input=sys.stdin.readline
cnt=0
def dfs(node):
    for n in mat[node]:
        if visit[n]==0:
            # print('visit[n]',visit[n],'visit[node]',visit[node])
            visit[n]=visit[node]+1
            dfs(n)
n=int(input())
p1,p2=map(int,input().split())
m=int(input())
mat=[[] for _ in range(n+1)]
visit=[0 for _ in range(n+1)]
for i in range(m):
    p,c=map(int,input().split())
    mat[p].append(c)
    mat[c].append(p)
dfs(p1)
print(visit[p2] if visit[p2]>0 else -1)
