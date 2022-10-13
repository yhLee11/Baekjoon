import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    tree=[[] for _ in range(N+1)]
    for _ in range(M):
        a,b=map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    # print(tree)
    v=[False]*(N+1)

    def dfs(start,cnt):
        v[start]=1
        for i in tree[start]:
            if not v[i]:
                cnt=dfs(i,cnt+1)
        return cnt
    res=dfs(1,0)
    print(res)