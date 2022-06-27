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
        hap=0
        for i in range(len(lst)):
            if hap+lst[i]>mid:
                hap=lst[i]
                cnt+=1
            else:
                hap+=lst[i]
        if hap:
            cnt+=1

        if cnt>m:
            left=mid+1
        else:
            right=mid-1
            ans=min(ans,mid)
        
bSearch(max(lst),sum(lst))
print(ans)