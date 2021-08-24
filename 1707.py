import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

k=int(input())
for i in range(k):
    v,e=map(int,input().split())
    arr=[[] for _ in range(v+1)]
    for j in range(e):
        n1,n2=map(int,input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)

    print(arr)

visit=[]
def dfs(v,group):
    visited[v]=group
    for i in graph[v]:
        if visited[i]==0:
            if not dfs(i,-group):
                return False
        elif visited[i]==visited[v]:
            return False
    return True

for _ in range(int(input())):
    v,e=map(int,input().split())
    graph=[[] for i in range(v+1)]
    visit=[0]*(v+1)
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(a)
        graph[b].append(b)
    bitpatile=True

    for i in range(1,v+1):
        if visit[i]==0:
            bitpatile=dfs(i,1)
            if not bitpatile:
                break
    print('YES' if bitpatile else 'NO')
    
