import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
city=[[sys.maxsize]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    city[a-1][b-1]=min(city[a-1][b-1],c)

for k in range(n):
    for s in range(n):
        for f in range(n):
            if s==f:city[s][f]=0
            if city[s][f]>city[s][k]+city[k][f]:
                city[s][f]=city[s][k]+city[k][f]
for c in city:
    print(*c)