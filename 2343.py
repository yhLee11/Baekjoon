import sys
input=sys.stdin.readline
n,m=map(int,input().split())
lst=list(map(int,input().split()))
ans=sys.maxsize
def bSearch(left,right):
    global ans
    while left<=right:
        mid=(left+right)//2
        cnt=0
        sum=0
        for i in range(len(lst)):
            if sum+lst[i]>mid:
                cnt+=1
                sum=0  
        if sum:
            cnt+=1
        if cnt>m:
            left=mid+1
        else:
            ans=min(ans,mid)
            right=mid-1
bSearch(max(lst),sum(lst))        
print(ans)