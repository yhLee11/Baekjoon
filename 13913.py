import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
#x-1,x+1,2x
visit=[0]*100001
path=[0]*100001
def bfs(start):
    q=deque()
    q.append(start)
    while q:
        cur=q.popleft()
        if cur==k:
            print(visit[cur])
            ans=[]
            while cur!=n:
                ans.append(cur)
                cur=path[cur]
            ans.append(n)
            ans.reverse()
            print(' '.join(map(str,ans)))
            return
        for nxt in (cur-1,cur+1,cur*2):
            if 0<=nxt<100001 and not visit[nxt]:
                visit[nxt]=visit[cur]+1
                path[nxt]=cur
                q.append(nxt)
bfs(n)