import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
parent=[i for i in range(N+1)]
weight=[]
for _ in range(M):
    a,b,c=map(int,input().split())
    weight.append((a,b,c))
weight.sort(key=lambda x:(x[2],x[0],x[1]))
# print(weight)
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
for a,b,c in weight:
    if find_parent(a)!=find_parent(b):
        union_parent(a,b)
        res+=c

print(res)