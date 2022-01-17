#https://jjangsungwon.tistory.com/4
import sys
input=sys.stdin.readline
n=int(input())
cost=[list(map(int,input().split(' '))) for _ in range(n)]
min_cost=sys.maxsize

def dfs(start,next,value,visit):
    global min_cost
    if len(visit)==n:
        if cost[next][start]!=0:
            min_cost=min(min_cost,value+cost[next][start])
        return

    for i in range(n):
        if cost[next][i]!=0 and i!=start and i not in visit:
            visit.append(i)
            dfs(start,i,value+cost[next][i],visit)
            visit.pop()

for i in range(n):
    dfs(i,i,0,[i])
print(min_cost)
