import sys
input=sys.stdin.readline
n,m=map(int,input().split())
start,end=0,0
numList=list(map(int,input().split()))
lstlen=len(numList)
num=0
ans=0
while True:
    if end==lstlen:
        if start==lstlen:
            break
        if m==num:
            ans+=1
        num-=numList[start]
        start+=1
    else:
        if num<m:
            num+=numList[end]
            end+=1
        elif num==m:
            num-=numList[start]
            ans+=1
            start+=1
            if end<start:
                end=start
        else:
            num-=numList[start]
            start+=1
    # print(start,end,'num=',num,'ans=',ans)
print(ans)
