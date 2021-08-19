import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
n=int(input())
tree=[[] for _ in range(n+1)]

for i in range(n-1):
    p,c,e=map(int,input().split())
    tree[p].append([c,c])
    tree[c].append([p,c])

weights=[0 for i in range(n+1)]

def dfs(start,tree,weights):
    for c,e in tree[start]:
        if weights[c]==0:
            weights[c]=weights[start]+e
            dfs(c,tree,weights)
dfs(1,tree,weights)
weights[1]=0
maxnum=0
maxidx=0
for i in range(len(weights)):
    if maxnum<weights[i]:
        maxnum=weights[i]
        maxidx=i
res=[0 for _ in range(n+1)]
dfs(maxidx,tree,res)
res[maxidx]=0
print(max(res))
"""
알고리즘 이해
:일단 트리의 지름을 구하려면 가장 끝 노드끼리 거리가 될거다.
거기서도 가장 큰 가중치(거리)를 가지는 것이 최종 지름이 된다.

1. 루트 1번을 시작으로 해서 가장 긴(먼 거리)에 있는
즉, 가중치가 큰 끝 노드를 DFS 탐색으로 찾는다.
2. 찾은 끝 노드를 다시 루트노드로 설정해 DFS 탐색을 한다.
3. 탐색하며 더한 가중치 값들 중 최댓값을 출력하면, 트리의 지름이 된다.

출처: https://fullmoon1344.tistory.com/114 [태야]
"""
