import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())
 
q=deque()
q.append(N)
v=[[-1,0] for _ in range(100001)]#방문시간, 방문수
v[N][0]=0
v[N][1]=1

while q:
    cur=q.popleft()
    for nxt in [cur-1,cur+1,cur*2]:
        if 0<=nxt<=100000:
            if v[nxt][0]==-1:#처음방문
                v[nxt][0]=v[cur][0]+1
                v[nxt][1]=1
                q.append(nxt)
            elif v[nxt][0]==v[cur][0]+1:#재방문이고 최단시간
                v[nxt][1]+=v[cur][1]
print(v[K][0])
print(v[K][1])