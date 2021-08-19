import sys
from collections import deque
sys.setrecursionlimit(100000)
input=sys.stdin.readline
cnt=0
stk=[]
def dfs(x,y):
    q=deque()
    q.append((x,0))
    while q:
        cur,dis=q.popleft()
        if cur==b:
            return dis
        for next in dic[cur]:
            if next==a:
                continue
            if visit[next]:
                continue
            visit[next]=1
            q.append((next,dis+1))
    return -1

n=int(input())
p1,p2=map(int,input().split())
m=int(input())
dic={}
visit=[0 for _ in range(n+1)]
for i in range(m):
    p,c=map(int,input().split())
    dic[p].append(c)
    dic[c].append(p)
