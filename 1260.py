from collections import deque, defaultdict
import sys
input=sys.stdin.readline

N,M,V=map(int,input().split())
graph=defaultdict(list)
for i in range(M):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(start):#V,하나부터 깊게 탐색
    stk=deque(sorted(graph[start],reverse=True))#리스트 들어감
    visit=[]
    visit.append(start)
    # print(visit,stk)
    while stk:
        node=stk.pop()
        if node not in visit:#방문한적없고,
            visit.append(node)
            stk+=sorted(list(set(graph[node])-set(visit)),reverse=True)
            # print(node,stk)
    return visit

def bfs(start):
    que=deque(sorted(graph[start]))
    visit=[]
    visit.append(start)
    # print(visit,que)
    while que:
        node=que.popleft()
        if node not in visit:
            visit.append(node)
            que+=sorted(list(set(graph[node])-set(visit)))
            # print(node,que)
    return visit
print(*dfs(V))
print(*bfs(V))
