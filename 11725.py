import sys
sys.setrecursionlimit(10**9)#재귀의 깊이
input=sys.stdin.readline
n=int(input())

tree={}
parents={}
for i in range(n):
    tree[i+1]=[]
    parents[i+1]=-1

for i in range(n-1):
    n1,n2=map(int,input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def dfs(start,tree,parents):
    for i in tree[start]:#연결된 노드 모두 탐색
        if parents[i]==-1:#한번도 방문한 적 없으면
            parents[i]=start#부모노드 저장
            dfs(i,tree,parents)
            
dfs(1,tree,parents)
for i in range(2,n+1):
    print(parents[i])
