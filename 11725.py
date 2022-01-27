import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
parents=[0 for _ in range(n+1)]
parents[1]=1
def dfs(start):
    for i in tree[start]:
        if parents[i]==0:
            parents[i]=start
            dfs(i)
dfs(1)
parents=parents[2:]
for i in parents:
    print(i)