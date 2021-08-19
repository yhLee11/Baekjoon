from collections import deque
import sys
input=sys.stdin.readline

N,M,V=map(int,input().split())

tree={}

for i in range(M):
    a,b=map(int,input().split())
    if a not in tree:
        tree[a]=[b]
    else:
        tree[a]+=[b]
    if b not in tree:
        tree[b]=[a]
    else:
        tree[b]+=[a]



def dfs(G,start):
    stack=[start]
    visit=[]

    while stack:
        node=stack.pop()
        if node not in visit:
            visit.append(node)
            if node in G:
                print(node)
                temp=list(set(G[node])-set(visit))
                temp.sort(reverse=True)
                print('dfs temp',temp)
                stack+=temp

    return " ".join(str(i) for i in visit)

def bfs(G,start):
    dq=deque([start])
    visit=[]

    while dq:
        node=dq.popleft()
        if node not in visit:
            visit.append(node)
            if node in G:
                print(node)
                temp=list(set(G[node])-set(visit))
                temp.sort()
                print('bfs temp',temp)
                dq+=temp
    return " ".join(str(i) for i in visit)

print(dfs(tree,V))
print(bfs(tree,V))
