import sys
input=sys.stdin.readline
N=int(input())
ans=0
money=1000-N
coin=[500,100,50,10,5,1]
idx=0
while money>0:
    mok,nam=divmod(money,coin[idx])
    ans+=mok
    money=nam
    idx+=1
print(ans)