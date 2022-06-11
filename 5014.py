import sys
from collections import deque
input=sys.stdin.readline
F,S,G,U,D=map(int,input().split())
mv=[U,-D]
cnt=0
def bfs(start,i):
    q=deque()
    q.append((start,i))
    visit=[False]*(F+1)
    visit[start]=True
    while q:
        cur,cnt=q.popleft()
        if cur==G:
            return print(cnt)
        for i in range(2):
            nxt=mv[i]+cur
            if 1<=nxt<=F and not visit[nxt]:
                visit[nxt]=True
                q.append((nxt,cnt+1))

    return print("use the stairs")

bfs(S,0)