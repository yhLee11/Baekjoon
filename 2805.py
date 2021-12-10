import sys
input=sys.stdin.readline
n,m=map(int,input().split())
heights=list(map(int,input().split()))
start,end=1,max(heights)

while start<=end:
    mid=(start+end)//2
    trees=0
    for i in heights:
        if i>mid:
            trees+=i-mid
    if trees>=m:
        start=mid+1
    else:
        end=mid-1
print(end)
