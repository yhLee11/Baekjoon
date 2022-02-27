import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
cost=[list(map(int,input().split())) for _ in range(n)]

for i in range(1,len(cost)):
    cost[i][0]=min(cost[i-1][1],cost[i-1][2])+cost[i][0]
    cost[i][1]=min(cost[i-1][0],cost[i-1][2])+cost[i][1]
    cost[i][2]=min(cost[i-1][0],cost[i-1][1])+cost[i][2]
    
print(min(cost[-1]))