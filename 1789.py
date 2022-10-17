import sys
input=sys.stdin.readline
N=int(input())
num=1
cnt=0
tmp=0
while tmp!=N:
    if tmp>N:
        cnt-=1
        break
    tmp+=num
    cnt+=1
    num+=1
print(cnt)