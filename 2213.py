import sys
input=sys.stdin.readline
n=int(input())
lst=map(int,input().split())
graph=[[] for _ in range(n+1)]
dp=[[0]*2 for _ in range(n+1)]
visit=[False for _ in range(n+1)]
num=[[[],[]] for _ in range(n+1)]
while True:
    try:
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    except:
        break
