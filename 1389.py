from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dic={}
INF=sys.maxsize
lst=[[INF]*n for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    lst[a-1][b-1]=1
    lst[b-1][a-1]=1
#     if a in dic:
#         dic[a]+=[b]
#     else:
#         dic[a]=[b]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                lst[i][j]=0
            else:
                lst[i][j]=min(lst[i][j],lst[i][k]+lst[k][j])
#print(lst)
res=[]
for i in lst:
    res.append(sum(i))
    #print(i)
#print(res)
for i in range(n):
    if res[i]==min(res):
        print(i+1)
        break
