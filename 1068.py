import sys
from collections import defaultdict as df
input=sys.stdin.readline
n=int(input())
prt=list(map(int,input().split()))
dnode=int(input())
tree=df(list)
for i in range(n):
    if i ==dnode or prt[i]==dnode:
        continue
    tree[prt[i]].append(i)
ans=0
# print(tree)
def dfs(node):
    global ans
    q=[]
    q.append(node)
    while q:
        nd=q.pop()
        # print(nd)
        if nd not in tree:
            ans+=1
        else:
            q.extend(tree[nd])
        # print(' ',ans)
    print(ans)
if -1 in tree:
    dfs(-1)
else:
    print(ans)    