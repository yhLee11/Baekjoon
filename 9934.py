import sys
input=sys.stdin.readline

k=int(input().strip())
lst=list(map(int,input().split()))
tree=[[] for _ in range(k)]

def bfs(lst,idx):
    mid=(len(lst)//2)
    tree[idx].append(lst[mid])
    if len(lst)==1:
        return
    bfs(lst[:mid],idx+1)
    bfs(lst[mid+1:],idx+1)
bfs(lst,0)
for i in range(k):
    print(*tree[i])

# idx=0
# for i in range(k):
#     cnt=0
#     while True:
#         if cnt==2:
#             res[k-i-1]+=[tree[idx]]
#             break
#         print(tree[idx])
#         res[k-i]+=[tree[idx]]
#         # res[k-i]+=list(tree[idx])
#         cnt+=1
#         idx+=1
