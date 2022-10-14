import sys
input=sys.stdin.readline
V,E=map(int,input().split())
tree=[]
parent=[i for i in range(V+1)]
for i in range(E):
    a,b,c=map(int,input().split())
    tree.append((c,a,b))
tree.sort(key=lambda x:(x[0],x[1],x[2]))

def find_parent(x):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a=find_parent(a)
    b=find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
res=0
for c,a,b in tree:
    if find_parent(a)!=find_parent(b):
        union_parent(a,b)
        res+=c
print(res)