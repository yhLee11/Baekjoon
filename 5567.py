import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
lst=[[] for _ in range(N+1)]
cnt=0
for _ in range(M):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
# print(lst)
v=[False]*(N+1)
v[1]=True
friend=set()
def dfs(start,ff):
    global cnt,v,friend
    if start!=1:
        friend.add(start)
    # print(start,ff,cnt,friend)
    if ff==2:
        return
    for i in lst[start]:
        if not v[i]:
            v[i]=True
            dfs(i,ff+1)
            v[i]=False
dfs(1,0)
print(len(friend))