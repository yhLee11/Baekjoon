import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
n=int(input())
tree=[[] for _ in range(n+1)]
parents=[0 for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
print(tree)
parents[1]=1
def dfs(start,tree,parents):
    for i in tree[start]:
        if parents[i]==0:
            parents[i]=start
            print(start,tree[start],i,parents)
            dfs(i,tree,parents)
dfs(1,tree,parents)

for i in range(2,n+1):
    print(parents[i])