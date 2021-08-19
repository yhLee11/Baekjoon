#독립집합 문제
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(input())
tree={}
for i in range(N):
    tree[i+1]=[]

graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)

while True:
    try:
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
        #tree[u]+=[v]
        #tree[v]+=[u]
    except:
        break
print(graph)
dp=[[0,0] for _ in range(N+1)]
print(dp)
def sol(num):
    visited[num]=True
    dp[num][0]=True
    dp[num][1]=1#얼리어답터 수?????
    for i in graph[num]:
        if not visited[i]:
            sol(i)
            dp[num][0]+=dp[i][1]
            dp[num][1]+=min(dp[i][0],dp[i][1])

sol(1)
print(dp,min(dp[1][0],dp[1][1]))
def dfs(start):
    stk=[start]
    visit=[]
    while stk:
        node=stk.pop()
        print('node',node)
        if node not in visit:
            visit.append(node)
            if node in tree:
                temp=list(set(tree[node])-set(visit))
                print('temp',temp)
                temp.sort(reverse=True)
                stk+=temp
                print('stk',stk)

    return " ".join(str(i) for i in visit)
# print(dfs(1))
