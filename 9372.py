from collections import deque
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

    def bfs(start):
        q=deque()
        q.append(start)
        v[start]=True
        cnt=0
        while q:
            cur=q.popleft()
            for i in tree[cur]:
                if not v[i]:
                    q.append(i)
                    v[i]=True
                    cnt+=1
        return cnt

    def dfs(start,cnt):
        v[start]=1
        for i in tree[start]:
            if not v[i]:
                cnt=dfs(i,cnt+1)
        return cnt
    # res=dfs(1,0)
    res=bfs(1)
    print(res)