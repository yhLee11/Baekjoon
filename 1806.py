import sys
input=sys.stdin.readline
n,s=map(int,input().split())
numList=list(map(int,input().split()))
start,end=0,0
num=0
ans=sys.maxsize
while True:
    if end==n:
        if start==n:break
        if s<=num:
            ans=min(ans,end-start)
        num-=numList[start]
        start+=1
    else:
        if num<s:
            num+=numList[end]
            end+=1
        elif num==s:
            num-=numList[start]
            ans=min(ans,end-start)
            start+=1
            if end<start:
                end=start
        else:
            ans=min(ans,end-start)
            num-=numList[start]
            start+=1
    # print(start,end,'num=',num,'ans=',ans)
if ans==sys.maxsize:
    print(0)
else:
    print(ans)
