import sys
from itertools import combinations
input=sys.stdin.readline
n,m=map(int,input().split())
city=[list(map(int,input().split())) for _ in range(n)]
ck_list=[]
h_list=[]
for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            h_list.append((i,j))
        elif city[i][j]==2:
            ck_list.append((i,j))

cmb=list(combinations(ck_list,m))
ans=sys.maxsize
for c in cmb:
    city_len=0
    # print(c)
    for h in h_list:
        h_min=sys.maxsize
        for ck in c:
            h_min=min(h_min,abs(h[0]-ck[0])+abs(h[1]-ck[1]))
        city_len+=h_min
    ans=min(city_len,ans)
print(ans)  