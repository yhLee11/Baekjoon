from itertools import combinations
import sys
import math
input=sys.stdin.readline
n,m=map(int,input().split())

chk_loc=[]
home_loc=[]
chk_street=[]

for i in range(n):
    line=list(map(int,input().split()))
    cnt=0
    for j in line:
        cnt+=1
        if j==1:
            home_loc.append([i+1,cnt])
        elif j==2:
            chk_loc.append((i+1,cnt))
comb=list(set(combinations(chk_loc,m)))
print('combinations',comb)
for i in comb:
    res=math.inf
    for one_ch in i:
        for one_h in home_loc:
            x=abs(one_h[0]-one_ch[0])
            y=abs(one_h[1]-one_ch[1])
            # res=min(res,x+y)
            res=x+y
            chk_street.append([one_ch,one_h,res])
            
print(chk_street)
# print('home',home_loc,'chk',chk_loc)

# for h in home_loc:
#     res=math.inf
#     for c in chk_loc:
#
#         x=abs(h[0]-c[0])
#         y=abs(h[1]-c[1])
#         res=min(res,x+y)
#     chk_street.append(res)
# print('minum chk_street (home->chk)',chk_street)
# chk_street=[]
# for c in chk_loc:
#     res=math.inf
#     one_ck=[]
#     for h in home_loc:
#         x=abs(h[0]-c[0])
#         y=abs(h[1]-c[1])
#         res=min(res,x+y)
#         one_ck.append(res)
#     chk_street.append(one_ck)
# print('chk_street -> one home',chk_street)
