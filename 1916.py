from collections import defaultdict
from hashlib import new
import heapq
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
INF=int(1e9)
dp=[INF for _ in range(n+1)]
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])

start,end=map(int,input().split())

def dijkstra(start):
    dp[start]=0
    h=[]
    heapq.heappush(h,[0,start])#우선순위,값
    while h:
        weight,number=heapq.heappop(h)
        if dp[number]<weight:
            continue
        for g_num,g_wei in graph[number]:
            new_wei=weight+g_wei
            if dp[g_num]>new_wei:
                dp[g_num]=new_wei
                heapq.heappush(h,[new_wei,g_num])
dijkstra(start)
print(dp[end])
